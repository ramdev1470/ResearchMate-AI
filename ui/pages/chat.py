"""Chat Page - ResearchMate AI"""

import streamlit as st
from ui.layouts import layout_header_section
from ui.theme import Icons

def render_chat_page():
    """Render chat page."""
    layout_header_section("Ask Questions", "Q&A about your research papers", Icons.CHAT)
    
    if not st.session_state.get("uploaded_documents"):
        st.warning("📚 Please upload papers first in the Upload tab")
        return
    
    # Chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # Display chat history
    st.markdown("### 💬 Conversation")
    
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            with st.chat_message("user", avatar="👤"):
                st.markdown(message["content"])
        else:
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(message["content"])
    
    # Use chat_input instead of text_input — it auto-clears after submit,
    # preventing the double-fire bug where Streamlit reruns with the
    # old value still in the widget.
    user_input = st.chat_input("Ask a question about your papers...")
    
    if user_input:
        # Add user message to history
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_input
        })
        
        # Display the user message immediately
        with st.chat_message("user", avatar="👤"):
            st.markdown(user_input)
        
        # Get response
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("🤖 Thinking..."):
                try:
                    response = _get_rag_response(user_input)
                    st.markdown(response)
                    
                    # Add assistant message to history
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": response
                    })
                    
                except Exception as e:
                    error_msg = f"❌ Error: {str(e)}"
                    st.error(error_msg)
    
    st.markdown("---")
    
    # Tips
    with st.expander("💡 Tips for Best Results"):
        st.markdown("""
        - **Be Specific** - Ask detailed questions
        - **Reference Papers** - Mention paper titles
        - **Key Terms** - Use domain-specific terminology
        - **Follow-up** - Ask clarifying questions
        """)


def _get_rag_response(question: str) -> str:
    """Get response using the RAG pipeline if available, else fall back to direct LLM."""
    from src.llm import get_llm
    
    # Try RAG pipeline first (uses ChromaDB retrieval)
    rag_chain = st.session_state.get("rag_chain")
    if rag_chain is not None:
        try:
            import logging
            logger = logging.getLogger(__name__)
            
            top_k = st.session_state.get("top_k", 5)
            rag_response = rag_chain.answer(question, top_k=top_k)
            
            if rag_response.answer and not rag_response.answer.startswith("No relevant documents"):
                logger.info(f"RAG response with {len(rag_response.sources)} sources, confidence={rag_response.confidence}")
                return rag_response.answer
        except Exception as e:
            import logging
            logging.getLogger(__name__).warning(f"RAG chain failed, falling back to direct LLM: {e}")
    
    # Fallback: direct LLM call with deduplicated context
    llm = get_llm()
    
    # Build context — deduplicate by filename to avoid sending the same paper twice
    seen_filenames = set()
    context_parts = []
    for doc in st.session_state.uploaded_documents:
        if doc.filename not in seen_filenames:
            seen_filenames.add(doc.filename)
            context_parts.append(f"{doc.filename}:\n{doc.text[:1500]}")
    
    context = "\n---\n".join(context_parts)
    
    response, confidence = llm.answer_question(question, context)
    return response