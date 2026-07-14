import logging
from typing import List
from src.models import RAGResponse, Citation
from src.llm import get_llm

logger = logging.getLogger(__name__)

class RAGChain:
    def __init__(self, retriever):
        self.retriever = retriever
        self.llm = get_llm()
        logger.info("RAGChain initialized")
    
    def answer(self, query: str, top_k: int = 5) -> RAGResponse:
        """Answer question using RAG."""
        try:
            results = self.retriever.retrieve(query, top_k=top_k)
            
            if not results:
                return RAGResponse(
                    answer="No relevant documents found.",
                    citations=[],
                    confidence=0.0
                )
            
            context = "\n\n".join([
                f"Source: {r['metadata'].get('source', 'unknown')}\n{r['content']}"
                for r in results
            ])
            
            answer, confidence = self.llm.answer_question(query, context)
            
            citations = [
                Citation(
                    source=r['metadata'].get('source', 'unknown'),
                    content=r['content'][:200],
                    format="APA"
                )
                for r in results[:3]
            ]
            
            return RAGResponse(
                answer=answer,
                citations=citations,
                confidence=confidence,
                sources=[r['metadata'].get('source', 'unknown') for r in results]
            )
        
        except Exception as e:
            logger.error(f"Error in RAG chain: {e}")
            return RAGResponse(
                answer=f"Error: {str(e)}",
                citations=[],
                confidence=0.0
            )
