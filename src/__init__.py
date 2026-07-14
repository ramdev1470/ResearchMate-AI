"""
ResearchMate AI - Source Package
"""

from src.config import settings
from src.models import PDFDocument, Summary, Citation, RAGResponse
from src.llm import LLMManager, get_llm
from src.pdf_loader import PDFLoader
from src.chunker import TextChunker
from src.embedding import EmbeddingManager
from src.vector_store import VectorStore
from src.retriever import Retriever
from src.rag_chain import RAGChain
from src.summarizer import Summarizer
from src.comparison import Comparator
from src.citation import CitationManager

__all__ = [
    'settings',
    'PDFDocument', 'Summary', 'Citation', 'RAGResponse',
    'LLMManager', 'get_llm',
    'PDFLoader',
    'TextChunker',
    'EmbeddingManager',
    'VectorStore',
    'Retriever',
    'RAGChain',
    'Summarizer',
    'Comparator',
    'CitationManager',
]
