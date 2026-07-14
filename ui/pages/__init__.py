"""ResearchMate AI - Pages Package"""

from ui.pages.dashboard import render_dashboard_page
from ui.pages.upload import render_upload_page
from ui.pages.chat import render_chat_page
from ui.pages.comparison import render_comparison_page
from ui.pages.summaries import render_summaries_page
from ui.pages.settings import render_settings_page

__all__ = [
    'render_dashboard_page',
    'render_upload_page',
    'render_chat_page',
    'render_comparison_page',
    'render_summaries_page',
    'render_settings_page',
]

# Page mapping
PAGES = {
    "Dashboard": render_dashboard_page,
    "Upload Papers": render_upload_page,
    "Chat": render_chat_page,
    "Comparison": render_comparison_page,
    "Summaries": render_summaries_page,
    "Settings": render_settings_page,
}

def get_page_function(page_name: str):
    """Get page render function by name."""
    return PAGES.get(page_name)

def get_all_pages():
    """Get all available pages."""
    return list(PAGES.keys())