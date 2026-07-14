"""Reusable UI Components for ResearchMate AI"""

import streamlit as st
from typing import Optional, List, Dict, Any

def render_header(title: str, subtitle: str = ""):
    """Render page header."""
    col1, col2 = st.columns([0.1, 0.9])
    with col1:
        st.markdown("📄")
    with col2:
        st.markdown(f"## {title}")
        if subtitle:
            st.markdown(f"*{subtitle}*")
    st.markdown("---")

def render_metric_row(metrics: Dict[str, Any]):
    """Render metrics in a row."""
    cols = st.columns(len(metrics))
    for col, (label, value) in zip(cols, metrics.items()):
        with col:
            st.metric(label, value)

def render_card(content: str, icon: str = "📋"):
    """Render a card with content."""
    st.markdown(f"""
    <div class="card">
    {icon} {content}
    </div>
    """, unsafe_allow_html=True)

def render_alert(message: str, alert_type: str = "info"):
    """Render an alert message."""
    icons = {
        "info": "ℹ️",
        "success": "✅",
        "warning": "⚠️",
        "error": "❌"
    }
    icon = icons.get(alert_type, "ℹ️")
    
    if alert_type == "success":
        st.success(f"{icon} {message}")
    elif alert_type == "warning":
        st.warning(f"{icon} {message}")
    elif alert_type == "error":
        st.error(f"{icon} {message}")
    else:
        st.info(f"{icon} {message}")

def render_button_group(buttons: List[Dict[str, Any]]):
    """Render a group of buttons."""
    cols = st.columns(len(buttons))
    for col, btn in zip(cols, buttons):
        with col:
            if st.button(btn['label'], key=btn.get('key'), use_container_width=True):
                if 'callback' in btn:
                    btn['callback']()

def render_section_divider(text: str = ""):
    """Render a section divider."""
    if text:
        st.markdown(f"### {text}")
    st.markdown("---")

def render_file_uploader(label: str = "Upload Files") -> List:
    """Render file uploader."""
    return st.file_uploader(label, type="pdf", accept_multiple_files=True)

def render_selectbox(label: str, options: List[str], key: str = None) -> str:
    """Render selectbox."""
    return st.selectbox(label, options, key=key)

def render_multiselect(label: str, options: List[str], default: List[str] = None, key: str = None) -> List[str]:
    """Render multiselect without problematic parameters."""
    return st.multiselect(label, options, default=default, key=key)

def render_text_input(label: str, placeholder: str = "", key: str = None) -> str:
    """Render text input."""
    return st.text_input(label, placeholder=placeholder, key=key)

def render_slider(label: str, min_val: float, max_val: float, default: float, key: str = None) -> float:
    """Render slider."""
    return st.slider(label, min_val, max_val, default, key=key)

def render_tabs(tabs: Dict[str, callable]):
    """Render tabs."""
    tab_list = st.tabs(list(tabs.keys()))
    for tab, (name, content_func) in zip(tab_list, tabs.items()):
        with tab:
            content_func()

def render_progress(value: float, label: str = ""):
    """Render progress bar."""
    st.progress(value)
    if label:
        st.caption(label)

def render_loading_spinner(text: str = "Loading..."):
    """Render loading spinner."""
    with st.spinner(text):
        return None

def render_success_message(message: str):
    """Render success message."""
    st.success(f"✅ {message}")

def render_error_message(message: str):
    """Render error message."""
    st.error(f"❌ {message}")

def render_warning_message(message: str):
    """Render warning message."""
    st.warning(f"⚠️ {message}")

def render_info_message(message: str):
    """Render info message."""
    st.info(f"ℹ️ {message}")

def render_expander(title: str, content: str):
    """Render expander."""
    with st.expander(f"📌 {title}"):
        st.markdown(content)

def render_code_block(code: str, language: str = "python"):
    """Render code block."""
    st.code(code, language=language)

def render_table(data: List[List], columns: List[str]):
    """Render table."""
    st.table({col: [row[i] for row in data] for i, col in enumerate(columns)})

def render_divider():
    """Render divider line."""
    st.divider()