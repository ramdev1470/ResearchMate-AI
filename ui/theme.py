"""Theme Configuration for ResearchMate AI"""

from enum import Enum

class Color(Enum):
    """Color palette."""
    PRIMARY = "#00d4ff"
    SECONDARY = "#1f77b4"
    DARK_BG = "#0e1419"
    CARD_BG = "#1a1f2e"
    TEXT_PRIMARY = "#ffffff"
    TEXT_SECONDARY = "#b0b8c1"
    BORDER = "#2d3748"
    SUCCESS = "#10b981"
    WARNING = "#f59e0b"
    ERROR = "#ef4444"

class Theme:
    """Theme configuration class."""
    
    # Colors
    PRIMARY_COLOR = Color.PRIMARY.value
    SECONDARY_COLOR = Color.SECONDARY.value
    DARK_BG = Color.DARK_BG.value
    CARD_BG = Color.CARD_BG.value
    TEXT_PRIMARY = Color.TEXT_PRIMARY.value
    TEXT_SECONDARY = Color.TEXT_SECONDARY.value
    BORDER_COLOR = Color.BORDER.value
    SUCCESS_COLOR = Color.SUCCESS.value
    WARNING_COLOR = Color.WARNING.value
    ERROR_COLOR = Color.ERROR.value
    
    # Spacing
    PADDING_XS = "4px"
    PADDING_SM = "8px"
    PADDING_MD = "16px"
    PADDING_LG = "24px"
    PADDING_XL = "32px"
    
    # Border Radius
    RADIUS_SM = "4px"
    RADIUS_MD = "8px"
    RADIUS_LG = "16px"
    
    # Font Sizes
    FONT_XS = "12px"
    FONT_SM = "14px"
    FONT_MD = "16px"
    FONT_LG = "20px"
    FONT_XL = "24px"
    
    # Font Weights
    WEIGHT_NORMAL = 400
    WEIGHT_MEDIUM = 500
    WEIGHT_SEMIBOLD = 600
    WEIGHT_BOLD = 700
    
    # Transitions
    TRANSITION_FAST = "0.15s"
    TRANSITION_NORMAL = "0.3s"
    TRANSITION_SLOW = "0.5s"
    
    # Shadows
    SHADOW_SM = "0 1px 2px rgba(0, 0, 0, 0.1)"
    SHADOW_MD = "0 4px 6px rgba(0, 0, 0, 0.1)"
    SHADOW_LG = "0 10px 15px rgba(0, 0, 0, 0.1)"

class Icons:
    """Icon definitions."""
    
    # Navigation
    DASHBOARD = "📊"
    UPLOAD = "📤"
    CHAT = "💬"
    COMPARE = "📊"
    SUMMARY = "📝"
    SETTINGS = "⚙️"
    
    # Actions
    PROCESS = "⚡"
    GENERATE = "✨"
    DOWNLOAD = "📥"
    UPLOAD_ARROW = "📤"
    DELETE = "🗑️"
    EDIT = "✏️"
    
    # Status
    SUCCESS = "✅"
    WARNING = "⚠️"
    ERROR = "❌"
    INFO = "ℹ️"
    LOADING = "⏳"
    
    # Documents
    PDF = "📄"
    FOLDER = "📁"
    FILE = "📋"
    
    # Misc
    ARROW_RIGHT = "→"
    ARROW_LEFT = "←"
    STAR = "⭐"
    FLAME = "🔥"
    ROCKET = "🚀"

class Fonts:
    """Font configuration."""
    MAIN = "'Inter', 'Segoe UI', sans-serif"
    MONO = "'Courier New', monospace"

def get_gradient(color1: str, color2: str) -> str:
    """Generate gradient CSS."""
    return f"linear-gradient(135deg, {color1} 0%, {color2} 100%)"

def get_box_shadow(elevation: int = 1) -> str:
    """Get box shadow based on elevation."""
    shadows = {
        0: "none",
        1: Theme.SHADOW_SM,
        2: Theme.SHADOW_MD,
        3: Theme.SHADOW_LG,
    }
    return shadows.get(elevation, Theme.SHADOW_MD)

def get_hover_effect(base_color: str) -> str:
    """Generate hover effect CSS."""
    return f"""
    transition: all {Theme.TRANSITION_NORMAL} ease;
    &:hover {{
        opacity: 0.8;
        transform: translateY(-2px);
        box-shadow: {Theme.SHADOW_LG};
    }}
    """