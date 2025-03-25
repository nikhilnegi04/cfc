"""
Theme configuration for the CFC Recovery Insights Dashboard.
Modify this file to change the dashboard's appearance.
"""

# Theme color configuration
THEME = {
    'PRIMARY': "#4A90E2",      # Blue - primary color
    'SECONDARY': "#50E3C2",    # Teal - secondary elements
    'ACCENT': "#FF6B6B",       # Coral - for alerts and highlights
    'WARNING': "#FFA726",      # Orange - for warnings
    'SUCCESS': "#66BB6A",      # Green - for positive indicators
    'BACKGROUND': "#F5F7FA",   # Light background
    'CARD': "#FFFFFF",         # Card background
    'TEXT': "#2C3E50",         # Primary text color
    'TEXT_LIGHT': "#7F8C8D"    # Secondary text color
}

def apply_theme_css():
    """
    Returns CSS styling for the dashboard based on the theme configuration.
    """
    return f"""
    <style>
        /* Base styles */
        body {{
            font-family: 'Roboto', sans-serif;
            background-color: {THEME['BACKGROUND']};
            color: {THEME['TEXT']};
        }}
        .main .block-container {{
            padding-top: 2rem;
            padding-bottom: 2rem;
        }}
        
        /* Card styling */
        .metric-card {{
            background-color: {THEME['CARD']};
            border-radius: 15px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
            padding: 25px;
            text-align: center;
            transition: all 0.3s ease;
        }}
        .metric-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
        }}
        .metric-value {{
            font-size: 36px;
            font-weight: 700;
            color: {THEME['PRIMARY']};
            margin-bottom: 10px;
        }}
        .metric-label {{
            font-size: 16px;
            color: {THEME['TEXT_LIGHT']};
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        /* Workload panel */
        .workload-panel {{
            background-color: {THEME['CARD']};
            border-left: 5px solid {THEME['PRIMARY']};
            border-radius: 15px;
            padding: 20px;
            margin-top: 25px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
        }}
        
        /* Metric pill */
        .metric-pill {{
            display: inline-block;
            padding: 6px 15px;
            border-radius: 30px;
            margin-right: 10px;
            margin-bottom: 10px;
            font-weight: 500;
            font-size: 14px;
            background-color: {THEME['SECONDARY']};
            color: {THEME['CARD']};
        }}
        
        /* Status box styling */
        .status-box {{
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 25px;
            display: flex;
            align-items: center;
            background-color: {THEME['CARD']};
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
        }}
        .status-icon {{
            font-size: 28px;
            margin-right: 15px;
        }}
        
        /* Chart area */
        .chart-area {{
            background-color: {THEME['CARD']};
            border-radius: 15px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
            padding: 25px;
            margin-top: 25px;
        }}
        
        /* Header */
        .dashboard-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
            padding: 20px;
            background-color: {THEME['CARD']};
            border-radius: 15px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
        }}
        .dashboard-title {{
            font-size: 42px;
            font-weight: 800;
            color: {THEME['PRIMARY']};
            margin: 0;
        }}
        .user-info {{
            text-align: right;
            font-size: 16px;
            color: {THEME['TEXT']};
        }}
        
        /* Recommendations panel */
        .recommendation-panel {{
            background-color: {THEME['CARD']};
            border-left: 5px solid {THEME['SECONDARY']};
            border-radius: 15px;
            padding: 20px;
            margin-top: 25px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
        }}
        
        /* Weekly summary */
        .weekly-summary {{
            background-color: {THEME['CARD']};
            border-radius: 15px;
            padding: 20px;
            margin-top: 25px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
        }}
        
        /* Footer */
        .dashboard-footer {{
            text-align: center;
            padding: 25px;
            color: {THEME['TEXT_LIGHT']};
            font-size: 14px;
            margin-top: 30px;
            background-color: {THEME['CARD']};
            border-radius: 15px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
        }}
    </style>
    """
