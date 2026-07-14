"""Comparison Page - ResearchMate AI"""

import streamlit as st
from ui.layouts import layout_header_section
from ui.theme import Icons

def render_comparison_page():
    """Render comparison page."""
    layout_header_section("Paper Comparison", "Compare multiple papers using OpenAI analysis", Icons.COMPARE)
    
    if not st.session_state.get("uploaded_documents"):
        st.warning("📚 Please upload at least 2 papers first in the Upload tab")
        return
    
    if len(st.session_state.uploaded_documents) < 2:
        st.warning(f"📚 Please upload at least 2 papers (currently have {len(st.session_state.uploaded_documents)})")
        return
    
    # Document selection
    st.markdown("### 📖 Select Papers to Compare")
    
    doc_names = [doc.filename for doc in st.session_state.uploaded_documents]
    
    selected_papers = st.multiselect(
        "Choose papers:",
        options=doc_names,
        default=doc_names[:2] if len(doc_names) >= 2 else doc_names,
        help="Select at least 2 papers to compare"
    )
    
    if len(selected_papers) < 2:
        st.info("⚠️ Please select at least 2 papers to compare")
        return
    
    st.markdown("---")
    
    # Comparison type
    st.markdown("### 🎯 Comparison Type")
    
    comparison_type = st.radio(
        "What to compare:",
        ["Methodology", "Key Findings", "Conclusions", "Overall Analysis"],
        horizontal=True,
        help="Select aspect of papers to compare"
    )
    
    st.markdown("---")
    
    # Run comparison
    if st.button("🚀 Compare with OpenAI", use_container_width=True):
        with st.spinner("🤖 Comparing papers..."):
            try:
                from src.comparison import Comparator
                from src.llm import get_llm
                
                comparator = Comparator()
                
                # Get selected documents
                selected_docs = [d for d in st.session_state.uploaded_documents if d.filename in selected_papers]
                
                # Extract content
                doc_contents = [doc.text[:3000] if hasattr(doc, 'text') else str(doc)[:3000] for doc in selected_docs]
                doc_titles = [doc.filename if hasattr(doc, 'filename') else str(doc) for doc in selected_docs]
                
                # Run comparison
                if comparison_type == "Methodology":
                    result = comparator.compare_methodologies(doc_contents, doc_titles)
                elif comparison_type == "Key Findings":
                    result = comparator.compare_findings(doc_contents, doc_titles)
                elif comparison_type == "Conclusions":
                    result = comparator.compare_conclusions(doc_contents, doc_titles)
                else:
                    result = comparator.comprehensive_comparison(doc_contents, doc_titles)
                
                st.markdown("---")
                st.markdown("### 📊 Comparison Results")
                st.markdown(result)
                
                # Download button
                st.download_button(
                    "📥 Download Comparison",
                    data=result,
                    file_name=f"comparison_{comparison_type.lower()}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    
    st.markdown("---")
    
    # Advanced Options
    with st.expander("⚙️ Advanced Options"):
        st.markdown("### Comparison Settings")
        
        analysis_depth = st.slider(
            "Analysis Depth:",
            min_value=1,
            max_value=5,
            value=3,
            help="1 = Brief, 5 = Comprehensive"
        )
        
        include_citations = st.checkbox("Include Citations", value=True)
        include_differences = st.checkbox("Highlight Differences", value=True)
        include_similarities = st.checkbox("Highlight Similarities", value=True)
        
        st.caption(f"Depth: {analysis_depth} | Citations: {include_citations} | Diff: {include_differences} | Sim: {include_similarities}")