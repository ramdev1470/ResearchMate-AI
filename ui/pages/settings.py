"""Settings Page - ResearchMate AI"""

import streamlit as st
from ui.layouts import layout_header_section
from ui.theme import Icons

def render_settings_page():
    """Render settings page."""
    layout_header_section("Settings", "Configure system parameters", Icons.SETTINGS)
    
    # Model Settings
    st.markdown("### 🤖 OpenAI Configuration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        model = st.selectbox(
            "Select Model:",
            ["gpt-3.5-turbo", "gpt-4-turbo", "gpt-4o"],
            help="Choose OpenAI model for responses"
        )
        st.session_state.model = model
    
    with col2:
        st.metric("Current Model", model)
    
    st.markdown("---")
    
    # Generation Parameters
    st.markdown("### ⚙️ Generation Parameters")
    
    temperature = st.slider(
        "Temperature (Creativity):",
        min_value=0.0,
        max_value=1.0,
        value=0.3,
        step=0.1,
        help="Lower = more factual, Higher = more creative"
    )
    st.session_state.temperature = temperature
    
    max_tokens = st.slider(
        "Max Tokens (Response Length):",
        min_value=100,
        max_value=4096,
        value=2048,
        step=100,
        help="Maximum tokens in response"
    )
    st.session_state.max_tokens = max_tokens
    
    st.markdown("---")
    
    # Retrieval Settings
    st.markdown("### 🔍 Retrieval Settings")
    
    top_k = st.slider(
        "Top-K Results:",
        min_value=1,
        max_value=20,
        value=5,
        help="Number of similar chunks to retrieve"
    )
    st.session_state.top_k = top_k
    
    threshold = st.slider(
        "Similarity Threshold:",
        min_value=0.0,
        max_value=1.0,
        value=0.3,
        step=0.05,
        help="Minimum similarity score"
    )
    
    st.markdown("---")
    
    # Display Settings
    st.markdown("### 🎨 Display Settings")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        show_embeddings = st.checkbox("Show Embeddings Info", value=False)
    
    with col2:
        show_timings = st.checkbox("Show Timings", value=True)
    
    with col3:
        show_metrics = st.checkbox("Show Metrics", value=True)
    
    st.markdown("---")
    
    # System Information
    st.markdown("### ℹ️ System Information")
    
    info_cols = st.columns(3)
    
    with info_cols[0]:
        st.metric("Papers Uploaded", len(st.session_state.get("uploaded_documents", [])))
    
    with info_cols[1]:
        st.metric("Current Model", model)
    
    with info_cols[2]:
        st.metric("Temperature", temperature)
    
    st.markdown("---")
    
    # API Status
    st.markdown("### 🔌 API Status")
    
    try:
        from src.llm import get_llm
        llm = get_llm()
        st.success("✅ OpenAI API connected")
        st.caption(f"Model: {llm.model}")
    except Exception as e:
        st.error(f"❌ API Error: {str(e)}")
    
    st.markdown("---")
    
    # Reset Settings
    st.markdown("### 🔄 Reset")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Reset to Defaults", use_container_width=True):
            st.session_state.temperature = 0.3
            st.session_state.max_tokens = 2048
            st.session_state.top_k = 5
            st.success("✅ Settings reset to defaults")
            st.rerun()
    
    with col2:
        if st.button("Clear Documents", use_container_width=True):
            st.session_state.uploaded_documents = []
            st.session_state.chat_history = []
            st.success("✅ All documents cleared")
            st.rerun()
    
    with col3:
        if st.button("Export Settings", use_container_width=True):
            settings_text = f"""ResearchMate AI Settings
Model: {model}
Temperature: {temperature}
Max Tokens: {max_tokens}
Top-K: {top_k}
Threshold: {threshold}
"""
            st.download_button(
                "Download Settings",
                data=settings_text,
                file_name="researchmate_settings.txt"
            )