import logging
from typing import List
from src.llm import get_llm

logger = logging.getLogger(__name__)

class Comparator:
    def __init__(self):
        self.llm = get_llm()
        logger.info("Comparator initialized")
    
    def compare_methodologies(self, docs_content: List[str], doc_titles: List[str]) -> str:
        """Compare methodologies."""
        formatted = self._format_docs(docs_content, doc_titles)
        prompt = f"Compare the research methodologies in these papers:\n\n{formatted}"
        return self.llm.generate_response(prompt)
    
    def compare_findings(self, docs_content: List[str], doc_titles: List[str]) -> str:
        """Compare findings."""
        formatted = self._format_docs(docs_content, doc_titles)
        prompt = f"Compare the key findings in these papers:\n\n{formatted}"
        return self.llm.generate_response(prompt)
    
    def compare_conclusions(self, docs_content: List[str], doc_titles: List[str]) -> str:
        """Compare conclusions."""
        formatted = self._format_docs(docs_content, doc_titles)
        prompt = f"Compare the conclusions in these papers:\n\n{formatted}"
        return self.llm.generate_response(prompt)
    
    def comprehensive_comparison(self, docs_content: List[str], doc_titles: List[str]) -> str:
        """Comprehensive comparison."""
        formatted = self._format_docs(docs_content, doc_titles)
        prompt = f"""Provide comprehensive comparison of these papers:
- Objectives and methodologies
- Key findings
- Conclusions
- Similarities and differences

Papers:
{formatted}"""
        return self.llm.generate_response(prompt)
    
    def _format_docs(self, contents: List[str], titles: List[str]) -> str:
        """Format documents for comparison."""
        formatted = []
        for title, content in zip(titles, contents):
            formatted.append(f"## {title}\n{content}")
        return "\n\n---\n\n".join(formatted)
