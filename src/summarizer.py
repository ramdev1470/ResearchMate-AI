import logging
from src.llm import get_llm
from src.models import Summary

logger = logging.getLogger(__name__)

class Summarizer:
    def __init__(self):
        self.llm = get_llm()
        logger.info("Summarizer initialized")
    
    def summarize(self, text: str, title: str = "Paper", max_length: int = 3000) -> Summary:
        """Summarize paper."""
        try:
            truncated_text = text[:max_length]
            
            prompt = f"""Summarize this research paper in 5-10 bullet points:

{truncated_text}

Format as bullet points starting with •"""
            
            summary_text = self.llm.generate_response(prompt)
            
            logger.info(f"Generated summary for {title}")
            
            return Summary(
                title=title,
                content=summary_text,
                source=title
            )
        
        except Exception as e:
            logger.error(f"Error summarizing: {e}")
            raise
