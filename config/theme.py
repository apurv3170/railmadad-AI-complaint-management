# config/theme.py
"""
Custom Theme Configuration for Rail Madad
Indian Railways Branding & Modern UI Design System
"""

# ==================== COLOR PALETTE ====================
# Indian Railways Official Colors
PRIMARY_COLOR = "#000080"      # Navy Blue
SECONDARY_COLOR = "#FF6600"    # Orange
ACCENT_COLOR = "#00A651"       # Green (for success states)

# Neutral Colors
BACKGROUND = "#FFFFFF"
SURFACE = "#F8F9FA"
SURFACE_DARK = "#E9ECEF"
TEXT_PRIMARY = "#212529"
TEXT_SECONDARY = "#6C757D"
BORDER_COLOR = "#DEE2E6"

# Status Colors
SUCCESS = "#28A745"
WARNING = "#FFC107"
ERROR = "#DC3545"
INFO = "#17A2B8"

# Gradient Backgrounds
GRADIENT_PRIMARY = "linear-gradient(135deg, #000080 0%, #0056b3 100%)"
GRADIENT_SECONDARY = "linear-gradient(135deg, #FF6600 0%, #ff8533 100%)"
GRADIENT_SURFACE = "linear-gradient(135deg, #F8F9FA 0%, #E9ECEF 100%)"

# ==================== TYPOGRAPHY ====================
FONT_FAMILY = "'Inter', 'Segoe UI', 'Roboto', sans-serif"
FONT_FAMILY_MONO = "'Fira Code', 'Consolas', monospace"

FONT_SIZES = {
    "xs": "0.75rem",    # 12px
    "sm": "0.875rem",   # 14px
    "base": "1rem",     # 16px
    "lg": "1.125rem",   # 18px
    "xl": "1.25rem",    # 20px
    "2xl": "1.5rem",    # 24px
    "3xl": "1.875rem",  # 30px
    "4xl": "2.25rem",   # 36px
}

FONT_WEIGHTS = {
    "normal": 400,
    "medium": 500,
    "semibold": 600,
    "bold": 700,
}

# ==================== SPACING ====================
SPACING = {
    "xs": "0.25rem",   # 4px
    "sm": "0.5rem",    # 8px
    "md": "1rem",      # 16px
    "lg": "1.5rem",    # 24px
    "xl": "2rem",      # 32px
    "2xl": "3rem",     # 48px
}

# ==================== BORDER RADIUS ====================
BORDER_RADIUS = {
    "sm": "0.25rem",   # 4px
    "md": "0.5rem",    # 8px
    "lg": "0.75rem",   # 12px
    "xl": "1rem",      # 16px
    "full": "9999px",  # Fully rounded
}

# ==================== SHADOWS ====================
SHADOWS = {
    "sm": "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
    "md": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    "lg": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
    "xl": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
}

# ==================== ANIMATIONS ====================
TRANSITIONS = {
    "fast": "all 0.15s ease-in-out",
    "base": "all 0.3s ease-in-out",
    "slow": "all 0.5s ease-in-out",
}

# ==================== CUSTOM CSS ====================
def get_custom_css():
    """Returns custom CSS for the application"""
    return f"""
    <style>
    /* ========== GLOBAL STYLES ========== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * {{
        font-family: {FONT_FAMILY};
    }}
    
    /* ========== STREAMLIT OVERRIDES ========== */
    .stApp {{
        background: {BACKGROUND};
    }}
    
    /* Hide Streamlit branding */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
    /* ========== CUSTOM COMPONENTS ========== */
    
    /* Card Component */
    .custom-card {{
        background: {SURFACE};
        border-radius: {BORDER_RADIUS['lg']};
        padding: {SPACING['lg']};
        box-shadow: {SHADOWS['md']};
        transition: {TRANSITIONS['base']};
        border: 1px solid {BORDER_COLOR};
    }}
    
    .custom-card:hover {{
        box-shadow: {SHADOWS['lg']};
        transform: translateY(-2px);
    }}
    
    /* Metric Card */
    .metric-card {{
        background: linear-gradient(135deg, {PRIMARY_COLOR} 0%, #0056b3 100%);
        color: white;
        border-radius: {BORDER_RADIUS['lg']};
        padding: {SPACING['lg']};
        box-shadow: {SHADOWS['lg']};
        text-align: center;
        transition: {TRANSITIONS['base']};
    }}
    
    .metric-card:hover {{
        transform: scale(1.05);
    }}
    
    .metric-value {{
        font-size: {FONT_SIZES['3xl']};
        font-weight: {FONT_WEIGHTS['bold']};
        margin: {SPACING['sm']} 0;
    }}
    
    .metric-label {{
        font-size: {FONT_SIZES['sm']};
        opacity: 0.9;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }}
    
    /* Status Badge */
    .status-badge {{
        display: inline-block;
        padding: {SPACING['xs']} {SPACING['sm']};
        border-radius: {BORDER_RADIUS['full']};
        font-size: {FONT_SIZES['xs']};
        font-weight: {FONT_WEIGHTS['semibold']};
        text-transform: uppercase;
        letter-spacing: 0.025em;
    }}
    
    .status-success {{
        background: {SUCCESS};
        color: white;
    }}
    
    .status-warning {{
        background: {WARNING};
        color: {TEXT_PRIMARY};
    }}
    
    .status-error {{
        background: {ERROR};
        color: white;
    }}
    
    .status-info {{
        background: {INFO};
        color: white;
    }}
    
    /* Button Styles */
    .custom-button {{
        background: {SECONDARY_COLOR};
        color: white;
        padding: {SPACING['sm']} {SPACING['lg']};
        border-radius: {BORDER_RADIUS['md']};
        border: none;
        font-weight: {FONT_WEIGHTS['semibold']};
        cursor: pointer;
        transition: {TRANSITIONS['fast']};
        box-shadow: {SHADOWS['sm']};
    }}
    
    .custom-button:hover {{
        background: #ff8533;
        box-shadow: {SHADOWS['md']};
        transform: translateY(-1px);
    }}
    
    .custom-button-outline {{
        background: transparent;
        color: {PRIMARY_COLOR};
        border: 2px solid {PRIMARY_COLOR};
        padding: {SPACING['sm']} {SPACING['lg']};
        border-radius: {BORDER_RADIUS['md']};
        font-weight: {FONT_WEIGHTS['semibold']};
        cursor: pointer;
        transition: {TRANSITIONS['fast']};
    }}
    
    .custom-button-outline:hover {{
        background: {PRIMARY_COLOR};
        color: white;
    }}
    
    /* Timeline Component */
    .timeline-item {{
        position: relative;
        padding-left: {SPACING['xl']};
        padding-bottom: {SPACING['lg']};
        border-left: 2px solid {BORDER_COLOR};
    }}
    
    .timeline-item:last-child {{
        border-left: none;
    }}
    
    .timeline-dot {{
        position: absolute;
        left: -6px;
        top: 0;
        width: 12px;
        height: 12px;
        border-radius: {BORDER_RADIUS['full']};
        background: {SECONDARY_COLOR};
        border: 2px solid {BACKGROUND};
    }}
    
    .timeline-content {{
        background: {SURFACE};
        padding: {SPACING['md']};
        border-radius: {BORDER_RADIUS['md']};
        box-shadow: {SHADOWS['sm']};
    }}
    
    /* Progress Bar */
    .progress-bar {{
        width: 100%;
        height: 8px;
        background: {SURFACE_DARK};
        border-radius: {BORDER_RADIUS['full']};
        overflow: hidden;
    }}
    
    .progress-fill {{
        height: 100%;
        background: {GRADIENT_SECONDARY};
        border-radius: {BORDER_RADIUS['full']};
        transition: width {TRANSITIONS['slow']};
    }}
    
    /* Alert Box */
    .alert {{
        padding: {SPACING['md']};
        border-radius: {BORDER_RADIUS['md']};
        border-left: 4px solid;
        margin: {SPACING['md']} 0;
    }}
    
    .alert-success {{
        background: rgba(40, 167, 69, 0.1);
        border-color: {SUCCESS};
        color: {SUCCESS};
    }}
    
    .alert-warning {{
        background: rgba(255, 193, 7, 0.1);
        border-color: {WARNING};
        color: #856404;
    }}
    
    .alert-error {{
        background: rgba(220, 53, 69, 0.1);
        border-color: {ERROR};
        color: {ERROR};
    }}
    
    .alert-info {{
        background: rgba(23, 162, 184, 0.1);
        border-color: {INFO};
        color: {INFO};
    }}
    
    /* Header Banner */
    .header-banner {{
        background: {GRADIENT_PRIMARY};
        color: white;
        padding: {SPACING['xl']} {SPACING['lg']};
        border-radius: {BORDER_RADIUS['lg']};
        margin-bottom: {SPACING['xl']};
        box-shadow: {SHADOWS['lg']};
    }}
    
    .header-title {{
        font-size: {FONT_SIZES['3xl']};
        font-weight: {FONT_WEIGHTS['bold']};
        margin-bottom: {SPACING['sm']};
    }}
    
    .header-subtitle {{
        font-size: {FONT_SIZES['lg']};
        opacity: 0.9;
    }}
    
    /* Data Table Styling */
    .dataframe {{
        border-radius: {BORDER_RADIUS['md']};
        overflow: hidden;
        box-shadow: {SHADOWS['md']};
    }}
    
    .dataframe thead th {{
        background: {PRIMARY_COLOR};
        color: white;
        font-weight: {FONT_WEIGHTS['semibold']};
        padding: {SPACING['md']};
    }}
    
    .dataframe tbody tr:hover {{
        background: {SURFACE};
    }}
    
    /* Form Styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {{
        border-radius: {BORDER_RADIUS['md']};
        border: 2px solid {BORDER_COLOR};
        transition: {TRANSITIONS['fast']};
    }}
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > select:focus {{
        border-color: {PRIMARY_COLOR};
        box-shadow: 0 0 0 3px rgba(0, 0, 128, 0.1);
    }}
    
    /* Sidebar Styling */
    .css-1d391kg {{
        background: {GRADIENT_SURFACE};
    }}
    
    /* Loading Skeleton */
    .skeleton {{
        background: linear-gradient(90deg, {SURFACE} 25%, {SURFACE_DARK} 50%, {SURFACE} 75%);
        background-size: 200% 100%;
        animation: loading 1.5s ease-in-out infinite;
        border-radius: {BORDER_RADIUS['md']};
    }}
    
    @keyframes loading {{
        0% {{ background-position: 200% 0; }}
        100% {{ background-position: -200% 0; }}
    }}
    
    /* Responsive Design */
    @media (max-width: 768px) {{
        .header-title {{
            font-size: {FONT_SIZES['2xl']};
        }}
        
        .custom-card {{
            padding: {SPACING['md']};
        }}
        
        .metric-card {{
            padding: {SPACING['md']};
        }}
    }}
    
    /* Utility Classes */
    .text-center {{ text-align: center; }}
    .text-right {{ text-align: right; }}
    .mt-1 {{ margin-top: {SPACING['sm']}; }}
    .mt-2 {{ margin-top: {SPACING['md']}; }}
    .mt-3 {{ margin-top: {SPACING['lg']}; }}
    .mb-1 {{ margin-bottom: {SPACING['sm']}; }}
    .mb-2 {{ margin-bottom: {SPACING['md']}; }}
    .mb-3 {{ margin-bottom: {SPACING['lg']}; }}
    .p-1 {{ padding: {SPACING['sm']}; }}
    .p-2 {{ padding: {SPACING['md']}; }}
    .p-3 {{ padding: {SPACING['lg']}; }}
    </style>
    """

# ==================== HELPER FUNCTIONS ====================
def apply_theme():
    """Apply custom theme to Streamlit app"""
    import streamlit as st
    st.markdown(get_custom_css(), unsafe_allow_html=True)

def get_status_color(status):
    """Get color for complaint status"""
    status_colors = {
        "pending": WARNING,
        "in_progress": INFO,
        "resolved": SUCCESS,
        "rejected": ERROR,
        "closed": TEXT_SECONDARY,
    }
    return status_colors.get(status.lower(), TEXT_SECONDARY)

def get_priority_color(priority):
    """Get color for priority level"""
    priority_colors = {
        "low": SUCCESS,
        "medium": WARNING,
        "high": ERROR,
        "critical": ERROR,
    }
    return priority_colors.get(priority.lower(), TEXT_SECONDARY)