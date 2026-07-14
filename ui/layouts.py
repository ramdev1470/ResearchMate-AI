"""Layout Components for ResearchMate AI"""

import streamlit as st
from typing import Dict, List, Callable
from ui.theme import Icons

def layout_main_page(page_config: Dict):
    """Configure main page layout."""
    st.set_page_config(
        page_title=page_config.get('title', 'ResearchMate AI'),
        page_icon=page_config.get('icon', '📄'),
        layout=page_config.get('layout', 'wide'),
        initial_sidebar_state=page_config.get('sidebar', 'expanded'),
        menu_items=page_config.get('menu_items')
    )

def layout_sidebar_navigation(pages: Dict[str, str]):
    """Create sidebar navigation."""
    with st.sidebar:
        st.markdown("# ResearchMate AI")
        st.markdown("#### Powered by OpenAI GPT-4o ⚡")
        st.markdown("---")
        
        selected = st.radio(
            "Select Page:",
            list(pages.keys()),
            format_func=lambda x: f"{pages[x]} {x}"
        )
        
        return selected

def layout_header_section(title: str, subtitle: str = "", icon: str = "📄"):
    """Create header section."""
    st.markdown(f"# {icon} {title}")
    if subtitle:
        st.markdown(f"*{subtitle}*")
    st.divider()

def layout_two_column(left_content: Callable, right_content: Callable, ratio: tuple = (1, 1)):
    """Create two-column layout."""
    col1, col2 = st.columns(ratio)
    with col1:
        left_content()
    with col2:
        right_content()

def layout_three_column(left: Callable, center: Callable, right: Callable, ratios: tuple = (1, 1, 1)):
    """Create three-column layout."""
    col1, col2, col3 = st.columns(ratios)
    with col1:
        left()
    with col2:
        center()
    with col3:
        right()

def layout_metric_cards(metrics: Dict[str, any]):
    """Display metrics in card layout."""
    cols = st.columns(len(metrics))
    for col, (label, value) in zip(cols, metrics.items()):
        with col:
            st.metric(label, value)

def layout_upload_section():
    """Create upload section layout."""
    st.markdown(f"### {Icons.UPLOAD} Upload Research Papers")
    
    uploaded_files = st.file_uploader(
        "Choose PDF files",
        type="pdf",
        accept_multiple_files=True,
        help="Upload one or more research papers in PDF format"
    )
    
    return uploaded_files

def layout_document_list(documents: List[Dict]):
    """Display list of uploaded documents."""
    st.markdown(f"### {Icons.FILE} Uploaded Documents")
    
    if not documents:
        st.info("No documents uploaded yet")
        return
    
    for i, doc in enumerate(documents):
        with st.expander(f"{Icons.PDF} {doc.get('filename', f'Document {i+1}')}"):
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.caption(f"**Title:** {doc.get('title', 'N/A')}")
                st.caption(f"**Pages:** {doc.get('num_pages', 'N/A')}")
            
            with col2:
                st.caption(f"**Size:** {doc.get('file_size_mb', 0):.1f} MB")
            
            with col3:
                if st.button("Delete", key=f"delete_{i}"):
                    st.rerun()

def layout_tabs_section(tabs: Dict[str, Callable]):
    """Create tabbed section layout."""
    tab_list = st.tabs(list(tabs.keys()))
    for tab, (name, content_func) in zip(tab_list, tabs.items()):
        with tab:
            content_func()

def layout_sidebar_stats(stats: Dict[str, any]):
    """Display stats in sidebar."""
    with st.sidebar:
        st.markdown("---")
        st.markdown("### 📊 Statistics")
        for label, value in stats.items():
            st.metric(label, value)

def layout_footer():
    """Display footer."""
    st.divider()
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.caption("📄 ResearchMate AI")
    with col2:
        st.caption("🤖 Powered by OpenAI")
    with col3:
        st.caption("⚡ Fast & Accurate")

def layout_dialog_box(title: str, content: str, buttons: Dict[str, Callable]):
    """Create dialog box layout."""
    st.markdown("---")
    st.markdown(f"### {title}")
    st.markdown(content)
    
    cols = st.columns(len(buttons))
    for col, (label, callback) in zip(cols, buttons.items()):
        with col:
            if st.button(label, use_container_width=True):
                callback()

def layout_feature_grid(features: List[Dict]):
    """Display features in grid layout."""
    cols = st.columns(len(features))
    for col, feature in zip(cols, features):
        with col:
            with st.container():
                st.markdown(f"### {feature.get('icon', '')} {feature.get('title', '')}")
                st.markdown(feature.get('description', ''))

def layout_progress_section(steps: List[Dict]):
    """Display progress steps."""
    st.markdown("### 📋 Progress")
    
    for i, step in enumerate(steps):
        col1, col2, col3 = st.columns([0.5, 2, 1])
        
        with col1:
            status_icon = "✅" if step.get('completed') else "⏳"
            st.markdown(f"### {status_icon}")
        
        with col2:
            st.markdown(f"**{step.get('title', '')}**")
            st.caption(step.get('description', ''))
        
        with col3:
            if step.get('progress'):
                st.progress(step['progress'])

def layout_comparison_view(left_doc: Dict, right_doc: Dict, analysis: str):
    """Display side-by-side comparison."""
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"### {left_doc.get('title', 'Document 1')}")
        st.markdown(left_doc.get('content', ''))
    
    with col2:
        st.markdown(f"### {right_doc.get('title', 'Document 2')}")
        st.markdown(right_doc.get('content', ''))
    
    st.markdown("---")
    st.markdown("### 🔍 Analysis")
    st.markdown(analysis)