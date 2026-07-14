import logging
from typing import List
from src.config import settings

logger = logging.getLogger(__name__)

class TextChunker:
    def __init__(self, chunk_size: int = None, overlap: int = None):
        self.chunk_size = chunk_size or settings.CHUNK_SIZE
        self.overlap = overlap or settings.CHUNK_OVERLAP
        logger.info(f"TextChunker initialized (size={self.chunk_size}, overlap={self.overlap})")
    
    def chunk(self, text: str, source: str = "unknown") -> List[dict]:
        """Split text into chunks."""
        if not text:
            return []
        
        chunks = []
        for i in range(0, len(text), self.chunk_size - self.overlap):
            chunk_text = text[i:i + self.chunk_size]
            chunks.append({
                "content": chunk_text,
                "source": source,
                "chunk_id": f"{source}_{len(chunks)}",
                "position": i
            })
        
        logger.info(f"Created {len(chunks)} chunks from {source}")
        return chunks
