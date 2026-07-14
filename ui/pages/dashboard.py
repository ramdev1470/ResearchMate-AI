"""Dashboard Page - ResearchMate AI"""

import streamlit as st
from ui.components import render_header, render_metric_row, render_alert, render_expander
from ui.layouts import layout_header_section, layout_metric_cards, layout_feature_grid
from ui.theme import Icons

def render_dashboard_page():
    """Render dashboard page."""
    layout_header_section("Dashboard", "System overview and quick stats", Icons.DASHBOARD)
    
    # Key Metrics
    st.markdown("### 📊 Key Metrics")
    metrics = {
        "Papers Uploaded": len(st.session_state.get("uploaded_documents", [])),
        "Current Model": st.session_state.get("model", "gpt-3.5-turbo"),
        "Temperature": st.session_state.get("temperature", 0.3),
    }
    layout_metric_cards(metrics)
    
    st.markdown("---")
    
    # Features Overview
    st.markdown("### ✨ Features")
    features = [
        {
            "icon": Icons.UPLOAD,
            "title": "Upload Papers",
            "description": "Load and process research PDFs instantly"
        },
        {
            "icon": Icons.SUMMARY,
            "title": "Quick Summaries",
            "description": "Generate summaries in 2-3 seconds with OpenAI"
        },
        {
            "icon": Icons.COMPARE,
            "title": "Compare Papers",
            "description": "Compare 2+ papers with AI-powered analysis"
        },
        {
            "icon": Icons.CHAT,
            "title": "Q&A Interface",
            "description": "Ask questions about your research papers"
        },
    ]
    layout_feature_grid(features)
    
    st.markdown("---")
    
    # Getting Started
    st.markdown("### 🚀 Getting Started")
    
    with st.expander("1. Upload Papers"):
        st.markdown("""
        - Click 'Upload Papers' in the navigation
        - Select one or more PDF files
        - Click 'Process Files (OpenAI)'
        - Wait for processing to complete
        """)
    
    with st.expander("2. Generate Summaries"):
        st.markdown("""
        - Go to 'Summaries' tab
        - Select a paper from dropdown
        - Click 'Generate Summary'
        - Summary appears in 2-3 seconds!
        """)
    
    with st.expander("3. Compare Papers"):
        st.markdown("""
        - Go to 'Comparison' tab
        - Select 2+ papers
        - Choose comparison type
        - Click 'Compare with OpenAI'
        - View comprehensive analysis
        """)
    
    with st.expander("4. Ask Questions"):
        st.markdown("""
        - Go to 'Chat' tab
        - Type your question
        - System searches uploaded papers
        - Get AI-powered answer with sources
        """)
    
    st.markdown("---")
    
    # System Information
    st.markdown("### ℹ️ System Information")
    
    info_cols = st.columns(3)
    
    with info_cols[0]:
        st.caption("**API Provider**")
        st.write("OpenAI GPT-4o")
    
    with info_cols[1]:
        st.caption("**Embedding Model**")
        st.write("Sentence Transformers")
    
    with info_cols[2]:
        st.caption("**Vector Database**")
        st.write("ChromaDB")
    
    st.markdown("---")
    
    # Tips & Tricks
    st.markdown("### 💡 Tips & Tricks")
    
    tips = [
        f"{Icons.FLAME} Use gpt-3.5-turbo for faster responses",
        f"{Icons.FLAME} Upload 3+ papers for better comparisons",
        f"{Icons.FLAME} Lower temperature for factual summaries",
        f"{Icons.FLAME} Higher temperature for creative analysis",
    ]
    
    for tip in tips:
        st.write(tip)
    
    st.markdown("---")
    
    # Call to Action
    st.markdown("### 🎯 What Next?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📤 Upload Papers", use_container_width=True):
            st.session_state.page = "Upload Papers"
            st.rerun()
    
    with col2:
        if st.button("📝 View Summaries", use_container_width=True):
            st.session_state.page = "Summaries"
            st.rerun()
    
    with col3:
        if st.button("⚙️ Settings", use_container_width=True):
            st.session_state.page = "Settings"
            st.rerun()