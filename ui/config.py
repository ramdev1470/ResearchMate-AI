"""UI Configuration for ResearchMate AI"""

from ui.theme import Theme, Icons

# Page Configuration
PAGE_CONFIG = {
    "title": "ResearchMate AI",
    "icon": "📄",
    "layout": "wide",
    "sidebar": "expanded",
    "menu_items": {
        "About": "ResearchMate AI - Research Paper Analysis with OpenAI GPT-4o"
    }
}

# Color Scheme
COLOR_SCHEME = {
    "primary": Theme.PRIMARY_COLOR,
    "secondary": Theme.SECONDARY_COLOR,
    "background": Theme.DARK_BG,
    "surface": Theme.CARD_BG,
    "text": Theme.TEXT_PRIMARY,
    "text_secondary": Theme.TEXT_SECONDARY,
    "border": Theme.BORDER_COLOR,
    "success": Theme.SUCCESS_COLOR,
    "warning": Theme.WARNING_COLOR,
    "error": Theme.ERROR_COLOR,
}

# Navigation Items
NAVIGATION_ITEMS = {
    "Dashboard": "📊",
    "Upload Papers": "📤",
    "Chat": "💬",
    "Comparison": "📊",
    "Summaries": "📝",
    "Settings": "⚙️",
}

# Sidebar Configuration
SIDEBAR_CONFIG = {
    "show_title": True,
    "title": "ResearchMate AI",
    "subtitle": "Powered by OpenAI GPT-4o ⚡",
    "show_divider": True,
    "show_stats": True,
    "width": 280,
}

# Dashboard Configuration
DASHBOARD_CONFIG = {
    "show_metrics": True,
    "metrics": ["Uploaded Papers", "Current Model", "Processing Speed"],
    "show_features": True,
    "features": [
        {
            "title": "📤 Upload Papers",
            "description": "Upload research PDFs and extract text"
        },
        {
            "title": "⚡ Fast Summaries",
            "description": "Generate summaries in 2-3 seconds"
        },
        {
            "title": "📊 Comparison",
            "description": "Compare multiple papers with AI analysis"
        },
        {
            "title": "💬 Q&A",
            "description": "Ask questions about your papers"
        },
    ]
}

# Upload Configuration
UPLOAD_CONFIG = {
    "show_file_list": True,
    "show_processing": True,
    "show_progress": True,
    "auto_process": False,
    "max_files": 10,
}

# Card Configuration
CARD_CONFIG = {
    "border_color": Theme.BORDER_COLOR,
    "background_color": Theme.CARD_BG,
    "border_radius": Theme.RADIUS_MD,
    "padding": Theme.PADDING_MD,
    "show_hover": True,
}

# Button Configuration
BUTTON_CONFIG = {
    "primary_color": Theme.PRIMARY_COLOR,
    "secondary_color": Theme.SECONDARY_COLOR,
    "border_radius": Theme.RADIUS_SM,
    "padding": Theme.PADDING_SM,
}

# Input Configuration
INPUT_CONFIG = {
    "background_color": Theme.CARD_BG,
    "text_color": Theme.TEXT_PRIMARY,
    "border_color": Theme.BORDER_COLOR,
    "focus_color": Theme.PRIMARY_COLOR,
    "border_radius": Theme.RADIUS_SM,
    "padding": Theme.PADDING_SM,
}

# Animation Configuration
ANIMATION_CONFIG = {
    "enable_animations": True,
    "transition_speed": Theme.TRANSITION_NORMAL,
    "enable_hover_effects": True,
    "enable_shadows": True,
}

# Responsive Configuration
RESPONSIVE_CONFIG = {
    "mobile_breakpoint": 768,
    "tablet_breakpoint": 1024,
    "desktop_breakpoint": 1280,
    "sidebar_collapse_mobile": True,
}

# Accessibility Configuration
ACCESSIBILITY_CONFIG = {
    "high_contrast": False,
    "large_text": False,
    "reduce_motion": False,
    "keyboard_navigation": True,
}

# Typography Configuration
TYPOGRAPHY_CONFIG = {
    "font_family": "'Inter', 'Segoe UI', sans-serif",
    "heading_size": Theme.FONT_XL,
    "body_size": Theme.FONT_MD,
    "caption_size": Theme.FONT_XS,
    "line_height": 1.5,
}

# Spacing Configuration
SPACING_CONFIG = {
    "gutter": Theme.PADDING_MD,
    "section_gap": Theme.PADDING_LG,
    "element_gap": Theme.PADDING_SM,
    "card_gap": Theme.PADDING_MD,
}

# Icons Configuration
ICONS_CONFIG = {
    "size": "24px",
    "color": Theme.TEXT_PRIMARY,
    "show_tooltips": True,
}

# Footer Configuration
FOOTER_CONFIG = {
    "show_footer": True,
    "show_links": True,
    "show_credits": True,
    "year": 2024,
}