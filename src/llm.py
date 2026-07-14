import logging
from openai import OpenAI
from src.config import settings

logger = logging.getLogger(__name__)

class LLMManager:
    def __init__(self):
        if not settings.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY not set in .env file")
        
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.PRIMARY_MODEL
        logger.info(f"LLMManager initialized with OpenAI - {self.model}")
    
    def answer_question(self, question: str, context: str) -> tuple:
        """Answer question using context with OpenAI."""
        prompt = f"""You are a research assistant. Based on the following context from research papers, answer the question accurately and concisely.

IMPORTANT INSTRUCTIONS:
- Synthesize information across all sources into a single coherent answer.
- Do NOT repeat the same point from different sources. Mention it once.
- Be concise and direct. Avoid redundancy.
- If sources contradict each other, note the disagreement once.

Context:
{context}

Question: {question}

Answer:"""
        
        try:
            import streamlit as st
            model = st.session_state.get("model", self.model)
            temperature = st.session_state.get("temperature", settings.TEMPERATURE)
            max_tokens = st.session_state.get("max_tokens", settings.MAX_TOKENS)
        except Exception:
            model = self.model
            temperature = settings.TEMPERATURE
            max_tokens = settings.MAX_TOKENS
            
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens,
                frequency_penalty=0.3
            )
            answer = response.choices[0].message.content
            return answer, 0.8
        except Exception as e:
            logger.error(f"Error in answer_question: {e}")
            raise

    def generate_response(self, prompt: str) -> str:
        """Generate response from OpenAI."""
        try:
            import streamlit as st
            model = st.session_state.get("model", self.model)
            temperature = st.session_state.get("temperature", settings.TEMPERATURE)
            max_tokens = st.session_state.get("max_tokens", settings.MAX_TOKENS)
        except Exception:
            model = self.model
            temperature = settings.TEMPERATURE
            max_tokens = settings.MAX_TOKENS

        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens,
                frequency_penalty=0.3
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error in generate_response: {e}")
            raise

    def summarize(self, text: str) -> str:
        """Summarize text using OpenAI."""
        prompt = f"""Summarize the following research paper in key bullet points:

{text[:3000]}

Summary:"""
        return self.generate_response(prompt)

_llm_instance = None

def get_llm():
    global _llm_instance
    if _llm_instance is None:
        _llm_instance = LLMManager()
    return _llm_instance
