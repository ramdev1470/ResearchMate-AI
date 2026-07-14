import logging
from typing import List
from src.config import settings

logger = logging.getLogger(__name__)

class Retriever:
    def __init__(self, vector_store, embedding_manager):
        self.vector_store = vector_store
        self.embedding_manager = embedding_manager
        logger.info("Retriever initialized")
    
    def retrieve(self, query: str, top_k: int = None, threshold: float = None) -> List[dict]:
        """Retrieve relevant chunks with deduplication."""
        try:
            top_k = top_k or settings.TOP_K_RETRIEVAL
            threshold = threshold or settings.RETRIEVAL_THRESHOLD
            
            query_embedding = self.embedding_manager.embed_text(query)
            
            # Fetch extra results so we still have enough after dedup
            results = self.vector_store.search(
                query_embedding=query_embedding,
                top_k=top_k + 3,
                threshold=threshold
            )
            
            # Deduplicate near-identical chunks
            deduped = self._deduplicate_results(results)
            
            logger.info(f"Retrieved {len(results)} results, {len(deduped)} after dedup for query")
            return deduped[:top_k]
        
        except Exception as e:
            logger.error(f"Error retrieving: {e}")
            return []
    
    def _deduplicate_results(self, results: List[dict], similarity_threshold: float = 0.8) -> List[dict]:
        """Remove near-duplicate chunks based on text overlap.
        
        Two chunks are considered duplicates if they share more than
        similarity_threshold fraction of their words.
        """
        if not results:
            return results
        
        deduped = [results[0]]
        
        for candidate in results[1:]:
            is_duplicate = False
            candidate_words = set(candidate['content'].lower().split())
            
            for existing in deduped:
                existing_words = set(existing['content'].lower().split())
                
                if not candidate_words or not existing_words:
                    continue
                
                overlap = len(candidate_words & existing_words)
                smaller_set = min(len(candidate_words), len(existing_words))
                
                if smaller_set > 0 and (overlap / smaller_set) > similarity_threshold:
                    is_duplicate = True
                    break
            
            if not is_duplicate:
                deduped.append(candidate)
        
        return deduped
