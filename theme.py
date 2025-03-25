# Updated theme.py
"""
Theme configuration for the CFC Recovery Insights Dashboard.
Modify this file to change the dashboard's appearance.
"""

# Theme color configuration
THEME = {
    'PRIMARY': "#123456",      # Darker blue - primary color (more focused)
    'SECONDARY': "#B3DAF1",    # Softer blue - secondary elements
    'ACCENT': "#E63946",       # Red - for alerts and highlights
    'WARNING': "#F4A261",      # Orange - for warnings
    'SUCCESS': "#2A9D8F",      # Green - for positive indicators
    'BACKGROUND': "#F8F9FA",   # Light background
    'CARD': "#FFFFFF",         # Card background
    'TEXT': "#123456",         # Darker primary text color
    'TEXT_LIGHT': "#6C757D"    # Secondary text color
}

def apply_theme_css():
    """
    Returns CSS styling for the dashboard based on the theme configuration.
    """
    return f"""
    <style>
        /* Base styles */
        .main .block-container {{
            padding-top: 2rem;
            padding-bottom: 2rem;
        }}
        
        /* Card styling with gradient */
        .metric-card {{
            background-color: {THEME['CARD']};
            background: linear-gradient(135deg, {THEME['CARD']} 0%, #f1f3f5 100%);
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 25px;
            text-align: center;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}
        .metric-card:hover {{
            transform: translateY(-8px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }}

        /* Workload panel */
        .workload-panel {{
            background-color: {THEME['CARD']};
            border-left: 6px solid {THEME['PRIMARY']};
            border-radius: 12px;
            padding: 20px;
            margin-top: 25px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        
        /* Refined metric pill */
        .metric-pill {{
            display: inline-block;
            padding: 6px 14px;
            border-radius: 50px;
            margin-right: 10px;
            margin-bottom: 10px;
            font-weight: 600;
            font-size: 15px;
            background-color: {THEME['SECONDARY']};
            color: {THEME['TEXT']};
        }}

        /* Larger metric value */
        .metric-value {{
            font-size: 32px;
            font-weight: 800;
            color: {THEME['PRIMARY']};
        }}
        
        /* Refined text labels */
        .metric-label {{
            font-size: 15px;
            color: {THEME['TEXT_LIGHT']};
            margin-bottom: 7px;
        }}

        /* Status box styling with accent border */
        .status-box {{
            padding: 22px;
            border-radius: 12px;
            border-left:
