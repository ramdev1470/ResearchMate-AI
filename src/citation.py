import logging
from typing import List
from src.models import Citation

logger = logging.getLogger(__name__)

class CitationManager:
    def __init__(self):
        logger.info("CitationManager initialized")
    
    def format_citation(self, citation: Citation, format_type: str = "APA") -> str:
        """Format citation."""
        if format_type == "APA":
            return f"{citation.source}. {citation.content}"
        elif format_type == "MLA":
            return f"{citation.source}. \"{citation.content}\""
        elif format_type == "Chicago":
            return f"{citation.source}: {citation.content}"
        else:
            return citation.source
    
    def format_multiple(self, citations: List[Citation], format_type: str = "APA") -> str:
        """Format multiple citations."""
        formatted = []
        for i, citation in enumerate(citations, 1):
            formatted_citation = self.format_citation(citation, format_type)
            formatted.append(f"{i}. {formatted_citation}")
        
        return "\n".join(formatted)
    
    def export_citations(self, citations: List[Citation], filename: str, format_type: str = "APA") -> bool:
        """Export citations to file."""
        try:
            formatted = self.format_multiple(citations, format_type)
            with open(filename, 'w') as f:
                f.write(f"Citations ({format_type} Format)\n")
                f.write("=" * 50 + "\n\n")
                f.write(formatted)
            
            logger.info(f"Exported citations to {filename}")
            return True
        except Exception as e:
            logger.error(f"Error exporting citations: {e}")
            return False
