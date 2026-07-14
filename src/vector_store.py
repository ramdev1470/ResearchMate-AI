import logging
from typing import List, Dict, Optional
import chromadb
from src.config import settings

logger = logging.getLogger(__name__)

class VectorStore:
    def __init__(self, persist_dir: str = None):
        self.persist_dir = persist_dir or settings.CHROMA_PERSIST_DIR
        try:
            self.client = chromadb.PersistentClient(path=self.persist_dir)
            self.collection = self.client.get_or_create_collection(
                name=settings.CHROMA_COLLECTION_NAME,
                metadata={"hnsw:space": "cosine"}
            )
            logger.info(f"VectorStore initialized at {self.persist_dir}")
        except Exception as e:
            logger.error(f"Error initializing VectorStore: {e}")
            raise
    
    def add(self, content: str, embedding: List[float], metadata: Optional[Dict] = None, doc_id: Optional[str] = None):
        """Add embedding to store."""
        try:
            if not doc_id:
                doc_id = f"doc_{len(self.collection.get()['ids'])}"
            
            self.collection.add(
                ids=[doc_id],
                embeddings=[embedding],
                documents=[content],
                metadatas=[metadata or {}]
            )
            logger.debug(f"Added {doc_id} to vector store")
        except Exception as e:
            logger.error(f"Error adding to vector store: {e}")
            raise
    
    def add_batch(self, contents: List[str], embeddings: List[List[float]], metadatas: Optional[List[Dict]] = None):
        """Add multiple embeddings."""
        try:
            import uuid
            ids = [f"doc_{uuid.uuid4().hex[:12]}" for _ in range(len(contents))]
            metadatas = metadatas or [{} for _ in contents]
            
            self.collection.add(
                ids=ids,
                embeddings=embeddings,
                documents=contents,
                metadatas=metadatas
            )
            logger.info(f"Added {len(contents)} items to vector store")
        except Exception as e:
            logger.error(f"Error batch adding: {e}")
            raise
    
    def search(self, query_embedding: List[float], top_k: int = 5, threshold: float = 0.0) -> List[Dict]:
        """Search vector store."""
        try:
            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=top_k
            )
            
            if not results or not results.get('documents'):
                return []
            
            documents = results['documents'][0]
            distances = results['distances'][0]
            metadatas = results['metadatas'][0]
            
            parsed_results = []
            for doc, distance, metadata in zip(documents, distances, metadatas):
                similarity = 1 - distance
                
                if similarity >= threshold:
                    parsed_results.append({
                        'content': doc,
                        'similarity': similarity,
                        'metadata': metadata
                    })
            
            return parsed_results
        
        except Exception as e:
            logger.error(f"Error searching vector store: {e}")
            return []
    
    def delete_all(self):
        """Clear collection."""
        try:
            self.client.delete_collection(name=settings.CHROMA_COLLECTION_NAME)
            self.collection = self.client.get_or_create_collection(
                name=settings.CHROMA_COLLECTION_NAME
            )
            logger.info("Cleared vector store")
        except Exception as e:
            logger.error(f"Error clearing: {e}")
            raise
