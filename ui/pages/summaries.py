"""Summaries Page - ResearchMate AI"""

import streamlit as st
from ui.layouts import layout_header_section
from ui.theme import Icons

def render_summaries_page():
    """Render summaries page."""
    layout_header_section("Paper Summaries", "Generate quick summaries with OpenAI", Icons.SUMMARY)
    
    if not st.session_state.get("uploaded_documents"):
        st.warning("📚 Please upload papers first in the Upload tab")
        return
    
    # Select paper
    st.markdown("### 📖 Select Paper")
    
    doc_names = [doc.filename for doc in st.session_state.uploaded_documents]
    selected_doc_name = st.selectbox("Choose a paper:", doc_names)
    
    selected_doc = next(d for d in st.session_state.uploaded_documents if d.filename == selected_doc_name)
    
    # Document info
    st.markdown("---")
    st.markdown("### 📋 Document Information")
    
    info_cols = st.columns(3)
    with info_cols[0]:
        st.metric("Title", selected_doc.title[:30] + "..." if len(selected_doc.title) > 30 else selected_doc.title)
    with info_cols[1]:
        st.metric("Pages", selected_doc.num_pages)
    with info_cols[2]:
        st.metric("Size", f"{selected_doc.file_size_mb:.1f} MB")
    
    st.markdown("---")
    
    # Generate summary
    st.markdown("### ⚡ Generate Summary")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("Click the button to generate a summary in 2-3 seconds")
    
    with col2:
        generate_btn = st.button("✨ Generate", use_container_width=True)
    
    if generate_btn:
        with st.spinner("🤖 Generating summary..."):
            try:
                from src.llm import get_llm
                
                llm = get_llm()
                summary_text = llm.summarize(selected_doc.text)
                
                st.markdown("---")
                st.markdown("### 📝 Summary")
                st.markdown(summary_text)
                
                # Download button
                st.download_button(
                    "📥 Download Summary",
                    data=summary_text,
                    file_name=f"summary_{selected_doc.filename}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    
    st.markdown("---")
    
    # Advanced Options
    with st.expander("⚙️ Advanced Options"):
        st.markdown("### Summary Configuration")
        
        format_type = st.radio(
            "Summary Format:",
            ["Bullet Points", "Paragraph", "Structured"],
            horizontal=True
        )
        
        length = st.slider("Summary Length:", 100, 500, 300)
        
        st.caption(f"Format: {format_type} | Length: {length} words")