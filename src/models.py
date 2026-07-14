from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class PDFDocument:
    filename: str
    filepath: str
    title: str
    text: str
    abstract: str = ""
    num_pages: int = 0
    file_size_mb: float = 0.0
    loaded_at: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class Summary:
    title: str
    content: str
    source: str = ""

@dataclass
class Citation:
    source: str
    content: str
    format: str = "APA"

@dataclass
class RAGResponse:
    answer: str
    citations: List[Citation] = field(default_factory=list)
    confidence: float = 0.8
    sources: List[str] = field(default_factory=list)
