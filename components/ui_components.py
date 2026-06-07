# components/ui_components.py
"""
Reusable UI Components for Rail Madad
Modern, professional components for B.Tech project
"""

import streamlit as st
from datetime import datetime
from typing import Optional, List, Dict, Any
import base64
from io import BytesIO

# ==================== METRIC CARDS ====================
def metric_card(label: str, value: str, delta: Optional[str] = None, 
                icon: Optional[str] = None, color: str = "#000080"):
    """
    Display a modern metric card with optional delta and icon
    
    Args:
        label: Metric label
        value: Metric value
        delta: Change indicator (e.g., "↑12%")
        icon: Emoji icon
        color: Background gradient color
    """
    delta_html = f"<div style='font-size: 0.875rem; opacity: 0.9;'>{delta}</div>" if delta else ""
    icon_html = f"<div style='font-size: 2rem; margin-bottom: 0.5rem;'>{icon}</div>" if icon else ""
    
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, {color} 0%, {color}CC 100%);
        color: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.3s ease;
    " onmouseover="this.style.transform='scale(1.05)'" 
       onmouseout="this.style.transform='scale(1)'">
        {icon_html}
        <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.9;">
            {label}
        </div>
        <div style="font-size: 2.25rem; font-weight: 700; margin: 0.5rem 0;">
            {value}
        </div>
        {delta_html}
    </div>
    """, unsafe_allow_html=True)

def metric_row(metrics: List[Dict[str, Any]], columns: int = 4):
    """
    Display multiple metrics in a row
    
    Args:
        metrics: List of metric dictionaries with keys: label, value, delta, icon, color
        columns: Number of columns
    """
    cols = st.columns(columns)
    for idx, metric in enumerate(metrics):
        with cols[idx % columns]:
            metric_card(
                label=metric.get('label', ''),
                value=metric.get('value', ''),
                delta=metric.get('delta'),
                icon=metric.get('icon'),
                color=metric.get('color', '#000080')
            )

# ==================== STATUS BADGES ====================
def status_badge(status: str, style: str = "default"):
    """
    Display a status badge
    
    Args:
        status: Status text
        style: Badge style (success, warning, error, info, default)
    """
    colors = {
        "success": ("#28A745", "white"),
        "warning": ("#FFC107", "#212529"),
        "error": ("#DC3545", "white"),
        "info": ("#17A2B8", "white"),
        "default": ("#6C757D", "white"),
        "pending": ("#FFC107", "#212529"),
        "in_progress": ("#17A2B8", "white"),
        "resolved": ("#28A745", "white"),
        "rejected": ("#DC3545", "white"),
    }
    
    bg_color, text_color = colors.get(style.lower(), colors["default"])
    
    return f"""
    <span style="
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        background: {bg_color};
        color: {text_color};
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.025em;
    ">{status}</span>
    """

# ==================== CUSTOM CARDS ====================
def custom_card(title: str, content: str, footer: Optional[str] = None, 
                icon: Optional[str] = None, action_button: Optional[Dict] = None):
    """
    Display a custom card with title, content, and optional footer
    
    Args:
        title: Card title
        content: Card content (HTML supported)
        footer: Card footer text
        icon: Emoji icon for title
        action_button: Dict with 'label' and 'callback' keys
    """
    icon_html = f"{icon} " if icon else ""
    footer_html = f"<div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #DEE2E6; font-size: 0.875rem; color: #6C757D;'>{footer}</div>" if footer else ""
    
    st.markdown(f"""
    <div style="
        background: #F8F9FA;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border: 1px solid #DEE2E6;
        transition: all 0.3s ease;
    " onmouseover="this.style.boxShadow='0 10px 15px rgba(0,0,0,0.1)'; this.style.transform='translateY(-2px)'" 
       onmouseout="this.style.boxShadow='0 4px 6px rgba(0,0,0,0.1)'; this.style.transform='translateY(0)'">
        <h3 style="margin: 0 0 1rem 0; color: #212529; font-weight: 600;">
            {icon_html}{title}
        </h3>
        <div style="color: #495057;">
            {content}
        </div>
        {footer_html}
    </div>
    """, unsafe_allow_html=True)
    
    if action_button:
        st.button(action_button['label'], key=f"btn_{title}", on_click=action_button.get('callback'))

# ==================== TIMELINE ====================
def timeline_item(title: str, description: str, timestamp: str, 
                  status: str = "default", is_last: bool = False):
    """
    Display a timeline item
    
    Args:
        title: Event title
        description: Event description
        timestamp: Event timestamp
        status: Status style (success, warning, error, info)
        is_last: Whether this is the last item
    """
    colors = {
        "success": "#28A745",
        "warning": "#FFC107",
        "error": "#DC3545",
        "info": "#17A2B8",
        "default": "#FF6600",
    }
    
    dot_color = colors.get(status.lower(), colors["default"])
    border_style = "none" if is_last else "2px solid #DEE2E6"
    
    st.markdown(f"""
    <div style="
        position: relative;
        padding-left: 2rem;
        padding-bottom: 1.5rem;
        border-left: {border_style};
    ">
        <div style="
            position: absolute;
            left: -6px;
            top: 0;
            width: 12px;
            height: 12px;
            border-radius: 9999px;
            background: {dot_color};
            border: 2px solid white;
        "></div>
        <div style="
            background: #F8F9FA;
            padding: 1rem;
            border-radius: 8px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        ">
            <div style="font-weight: 600; color: #212529; margin-bottom: 0.25rem;">
                {title}
            </div>
            <div style="font-size: 0.875rem; color: #495057; margin-bottom: 0.5rem;">
                {description}
            </div>
            <div style="font-size: 0.75rem; color: #6C757D;">
                {timestamp}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def timeline(events: List[Dict[str, str]]):
    """
    Display a complete timeline
    
    Args:
        events: List of event dicts with keys: title, description, timestamp, status
    """
    for idx, event in enumerate(events):
        timeline_item(
            title=event.get('title', ''),
            description=event.get('description', ''),
            timestamp=event.get('timestamp', ''),
            status=event.get('status', 'default'),
            is_last=(idx == len(events) - 1)
        )

# ==================== PROGRESS BAR ====================
def progress_bar(value: int, max_value: int = 100, label: Optional[str] = None, 
                 color: str = "#FF6600"):
    """
    Display a custom progress bar
    
    Args:
        value: Current value
        max_value: Maximum value
        label: Optional label
        color: Progress bar color
    """
    percentage = int((value / max_value) * 100)
    label_html = f"<div style='margin-bottom: 0.5rem; font-weight: 500;'>{label}</div>" if label else ""
    
    st.markdown(f"""
    {label_html}
    <div style="
        width: 100%;
        height: 8px;
        background: #E9ECEF;
        border-radius: 9999px;
        overflow: hidden;
    ">
        <div style="
            width: {percentage}%;
            height: 100%;
            background: linear-gradient(90deg, {color} 0%, {color}CC 100%);
            border-radius: 9999px;
            transition: width 0.5s ease;
        "></div>
    </div>
    <div style="margin-top: 0.25rem; font-size: 0.75rem; color: #6C757D;">
        {value} / {max_value} ({percentage}%)
    </div>
    """, unsafe_allow_html=True)

# ==================== ALERT BOXES ====================
def alert(message: str, alert_type: str = "info", dismissible: bool = False):
    """
    Display an alert box
    
    Args:
        message: Alert message
        alert_type: Type (success, warning, error, info)
        dismissible: Whether alert can be dismissed
    """
    colors = {
        "success": ("#28A745", "rgba(40, 167, 69, 0.1)", "✅"),
        "warning": ("#856404", "rgba(255, 193, 7, 0.1)", "⚠️"),
        "error": ("#DC3545", "rgba(220, 53, 69, 0.1)", "❌"),
        "info": ("#17A2B8", "rgba(23, 162, 184, 0.1)", "ℹ️"),
    }
    
    text_color, bg_color, icon = colors.get(alert_type.lower(), colors["info"])
    
    st.markdown(f"""
    <div style="
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid {text_color};
        background: {bg_color};
        color: {text_color};
        margin: 1rem 0;
    ">
        {icon} {message}
    </div>
    """, unsafe_allow_html=True)

# ==================== HEADER BANNER ====================
def header_banner(title: str, subtitle: Optional[str] = None, 
                  icon: Optional[str] = None):
    """
    Display a header banner with gradient background
    
    Args:
        title: Main title
        subtitle: Subtitle text
        icon: Emoji icon
    """
    icon_html = f"<span style='margin-right: 0.5rem;'>{icon}</span>" if icon else ""
    subtitle_html = f"<div style='font-size: 1.125rem; opacity: 0.9; margin-top: 0.5rem;'>{subtitle}</div>" if subtitle else ""
    
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #000080 0%, #0056b3 100%);
        color: white;
        padding: 2rem 1.5rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 15px rgba(0,0,0,0.1);
    ">
        <div style="font-size: 1.875rem; font-weight: 700;">
            {icon_html}{title}
        </div>
        {subtitle_html}
    </div>
    """, unsafe_allow_html=True)

# ==================== QUICK ACTION BUTTONS ====================
def action_button(label: str, icon: Optional[str] = None, 
                  style: str = "primary", full_width: bool = False):
    """
    Display a custom styled button
    
    Args:
        label: Button label
        icon: Emoji icon
        style: Button style (primary, secondary, outline)
        full_width: Whether button should be full width
    """
    styles = {
        "primary": ("white", "#FF6600", "#ff8533"),
        "secondary": ("white", "#000080", "#0056b3"),
        "outline": ("#000080", "transparent", "#000080"),
    }
    
    text_color, bg_color, hover_bg = styles.get(style, styles["primary"])
    width = "100%" if full_width else "auto"
    icon_html = f"{icon} " if icon else ""
    border = f"2px solid {text_color}" if style == "outline" else "none"
    
    return st.markdown(f"""
    <button style="
        background: {bg_color};
        color: {text_color};
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        border: {border};
        font-weight: 600;
        cursor: pointer;
        transition: all 0.15s ease;
        width: {width};
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    " onmouseover="this.style.background='{hover_bg}'; this.style.boxShadow='0 4px 6px rgba(0,0,0,0.1)'; this.style.transform='translateY(-1px)'"
       onmouseout="this.style.background='{bg_color}'; this.style.boxShadow='0 1px 2px rgba(0,0,0,0.05)'; this.style.transform='translateY(0)'">
        {icon_html}{label}
    </button>
    """, unsafe_allow_html=True)

# ==================== COMPLAINT CARD ====================
def complaint_card(complaint_id: str, title: str, category: str, 
                   status: str, date: str, priority: str = "medium"):
    """
    Display a complaint card with all details
    
    Args:
        complaint_id: Complaint ID
        title: Complaint title
        category: Complaint category
        status: Current status
        date: Filed date
        priority: Priority level
    """
    priority_colors = {
        "low": "#28A745",
        "medium": "#FFC107",
        "high": "#DC3545",
        "critical": "#DC3545",
    }
    
    priority_color = priority_colors.get(priority.lower(), "#6C757D")
    status_badge_html = status_badge(status, status.lower())
    
    st.markdown(f"""
    <div style="
        background: #F8F9FA;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-left: 4px solid {priority_color};
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    " onmouseover="this.style.boxShadow='0 10px 15px rgba(0,0,0,0.1)'; this.style.transform='translateY(-2px)'"
       onmouseout="this.style.boxShadow='0 4px 6px rgba(0,0,0,0.1)'; this.style.transform='translateY(0)'">
        <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.75rem;">
            <div>
                <div style="font-weight: 600; font-size: 0.875rem; color: #6C757D;">
                    {complaint_id}
                </div>
                <div style="font-weight: 600; font-size: 1.125rem; color: #212529; margin-top: 0.25rem;">
                    {title}
                </div>
            </div>
            {status_badge_html}
        </div>
        <div style="display: flex; gap: 1rem; font-size: 0.875rem; color: #6C757D;">
            <div>📁 {category}</div>
            <div>📅 {date}</div>
            <div>⚡ {priority.upper()}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==================== EMPTY STATE ====================
def empty_state(icon: str, title: str, message: str, 
                action_label: Optional[str] = None):
    """
    Display an empty state placeholder
    
    Args:
        icon: Emoji icon
        title: Title text
        message: Description message
        action_label: Optional action button label
    """
    action_html = f"""
    <button style="
        margin-top: 1rem;
        background: #FF6600;
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        border: none;
        font-weight: 600;
        cursor: pointer;
    ">{action_label}</button>
    """ if action_label else ""
    
    st.markdown(f"""
    <div style="
        text-align: center;
        padding: 3rem 1.5rem;
        color: #6C757D;
    ">
        <div style="font-size: 4rem; margin-bottom: 1rem;">
            {icon}
        </div>
        <div style="font-size: 1.5rem; font-weight: 600; color: #495057; margin-bottom: 0.5rem;">
            {title}
        </div>
        <div style="font-size: 1rem;">
            {message}
        </div>
        {action_html}
    </div>
    """, unsafe_allow_html=True)

# ==================== LOADING SKELETON ====================
def loading_skeleton(height: str = "100px", count: int = 1):
    """
    Display loading skeleton placeholders
    
    Args:
        height: Height of skeleton
        count: Number of skeletons
    """
    for _ in range(count):
        st.markdown(f"""
        <div style="
            height: {height};
            background: linear-gradient(90deg, #F8F9FA 25%, #E9ECEF 50%, #F8F9FA 75%);
            background-size: 200% 100%;
            animation: loading 1.5s ease-in-out infinite;
            border-radius: 8px;
            margin-bottom: 1rem;
        "></div>
        <style>
        @keyframes loading {{
            0% {{ background-position: 200% 0; }}
            100% {{ background-position: -200% 0; }}
        }}
        </style>
        """, unsafe_allow_html=True)