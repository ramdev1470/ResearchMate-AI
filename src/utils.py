import logging
from pathlib import Path
from typing import List

logger = logging.getLogger(__name__)

def validate_pdf(filepath: str) -> bool:
    """Validate PDF file."""
    path = Path(filepath)
    return path.exists() and path.suffix.lower() == '.pdf'

def format_file_size(size_bytes: float) -> str:
    """Format bytes to human readable."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"

def truncate_text(text: str, max_length: int = 100) -> str:
    """Truncate text."""
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."

def chunk_list(lst: List, chunk_size: int) -> List[List]:
    """Split list into chunks."""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def log_operation(operation: str, status: str = "SUCCESS"):
    """Log operation."""
    logger.info(f"{operation}: {status}")
