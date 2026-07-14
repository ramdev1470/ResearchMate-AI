import logging
from pathlib import Path
import fitz
from src.models import PDFDocument
from src.config import settings

logger = logging.getLogger(__name__)

class PDFLoader:
    def __init__(self):
        self.max_size_mb = settings.MAX_PDF_SIZE_MB
        logger.info("PDFLoader initialized")
    
    def load(self, filepath: str) -> PDFDocument:
        """Load PDF and extract text."""
        path = Path(filepath)
        
        if not path.exists():
            raise FileNotFoundError(f"File not found: {filepath}")
        
        if path.suffix.lower() != '.pdf':
            raise ValueError(f"Not a PDF file: {filepath}")
        
        size_mb = path.stat().st_size / (1024 * 1024)
        if size_mb > self.max_size_mb:
            raise ValueError(f"File too large: {size_mb:.1f} MB")
        
        doc = fitz.open(str(path))
        num_pages = len(doc)
        
        text = ""
        for page in doc:
            text += page.get_text()
        
        metadata = doc.metadata or {}
        title = metadata.get("title", path.stem)
        
        doc.close()
        
        abstract = text[:500] if text else ""
        
        logger.info(f"Loaded {path.name} ({num_pages} pages)")
        
        return PDFDocument(
            filename=path.name,
            filepath=str(path),
            title=title,
            text=text,
            abstract=abstract,
            num_pages=num_pages,
            file_size_mb=size_mb
        )
