import os
import streamlit as st
import logging
from src.config import settings
from src.llm import get_llm
from ui.pages import get_page_function
from ui.layouts import layout_footer

# Configure logging
logging.basicConfig(level=settings.LOG_LEVEL)
logger = logging.getLogger(__name__)

# Load CSS custom styling
def load_css():
    css_path = os.path.join("ui", "styles.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Page config
st.set_page_config(
    page_title="ResearchMate AI",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply premium CSS styles
load_css()

# Initialize session state variables
if "uploaded_documents" not in st.session_state:
    st.session_state.uploaded_documents = []
if "llm" not in st.session_state:
    st.session_state.llm = get_llm()
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# Set up settings defaults in session state if not already set
if "model" not in st.session_state:
    st.session_state.model = settings.PRIMARY_MODEL
if "temperature" not in st.session_state:
    st.session_state.temperature = settings.TEMPERATURE
if "max_tokens" not in st.session_state:
    st.session_state.max_tokens = settings.MAX_TOKENS
if "top_k" not in st.session_state:
    st.session_state.top_k = settings.TOP_K_RETRIEVAL

# Sidebar Navigation Handler
def on_nav_change():
    st.session_state.page = st.session_state.nav_radio

with st.sidebar:
    st.markdown("# ResearchMate AI")
    st.markdown("#### Powered by OpenAI GPT-4o ⚡")
    st.markdown("---")
    
    nav_options = {
        "Dashboard": "📊 Dashboard",
        "Upload Papers": "📤 Upload Papers",
        "Chat": "💬 Chat",
        "Comparison": "⚖️ Comparison",
        "Summaries": "📝 Summaries",
        "Settings": "⚙️ Settings",
    }
    
    # Resolve index dynamically for programmatic page redirects
    keys_list = list(nav_options.keys())
    current_idx = keys_list.index(st.session_state.page) if st.session_state.page in keys_list else 0
    
    selected_nav = st.radio(
        "Select Page:",
        options=keys_list,
        format_func=lambda x: nav_options[x],
        index=current_idx,
        key="nav_radio",
        on_change=on_nav_change
    )
    
    st.session_state.page = selected_nav
    
    st.markdown("---")
    st.markdown("### 📊 Documents")
    st.metric("Uploaded Papers", len(st.session_state.uploaded_documents))

# Render main page content dynamically
page_func = get_page_function(st.session_state.page)
if page_func:
    try:
        page_func()
    except Exception as e:
        st.error(f"❌ Error rendering page: {str(e)}")
        logger.exception("Error rendering page")
else:
    st.error(f"Page '{st.session_state.page}' not found.")

# Render footer layout
layout_footer()
