def render_match_readiness_dashboard(all_player_data, risk_threshold):
    """
    Render the match readiness dashboard section with improved visual appeal
    
    Parameters:
    all_player_data (DataFrame): Recovery data for all players
    risk_threshold (float): Threshold for determining risk
    """
    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #4A90E2;
    }
    .medium-font {
        font-size:20px !important;
        font-weight: bold;
        color: #50E3C2;
    }
    .small-font {
        font-size:16px !important;
        color: #2C3E50;
    }
    .info-box {
        background-color: #F5F7FA;
        border-left: 5px solid #4A90E2;
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<p class='big-font'>Match Readiness Dashboard</p>", unsafe_allow_html=True)

    # Calculate player readiness
    player_groups = all_player_data.groupby("player_name")
    player_readiness = [calculate_player_readiness(group, risk_threshold) for _, group in player_groups]

    # Get squad recommendations
    squad_recommendations = get_squad_recommendations(all_player_data, risk_threshold)

    # Display team overview
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<p class='medium-font'>Team Overview</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='small-font'>Players Improving: {squad_recommendations['improving_count']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='small-font'>Players Declining: {squad_recommendations['declining_count']}</p>", unsafe_allow_html=True)

    with col2:
        st.markdown("<p class='medium-font'>Squad Status</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='small-font'>Starting XI: {len(squad_recommendations['starting_xi'])}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='small-font'>Bench: {len(squad_recommendations['bench'])}</p>", unsafe_allow_html=True)

    with col3:
        st.markdown("<p class='medium-font'>Bench Coverage</p>", unsafe_allow_html=True)
        for position, covered in squad_recommendations['positions_covered'].items():
            status = "✅" if covered else "❌"
            st.markdown(f"<p class='small-font'>{position}: {status}</p>", unsafe_allow_html=True)

    # Display team readiness chart
    st.markdown("<p class='medium-font'>Team Readiness Chart</p>", unsafe_allow_html=True)
    fig = create_team_readiness_chart(player_readiness)
    st.plotly_chart(fig, use_container_width=True)

    # Display starting XI and bench
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<p class='medium-font'>Starting XI</p>", unsafe_allow_html=True)
        for player in squad_recommendations['starting_xi']:
            st.markdown(f"<div class='info-box'><p class='small-font'><b>{player['player_name']}</b> ({player['position']})<br>Readiness: {player['readiness_score']:.1f}%</p></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<p class='medium-font'>Bench</p>", unsafe_allow_html=True)
        for player in squad_recommendations['bench']:
            st.markdown(f"<div class='info-box'><p class='small-font'><b>{player['player_name']}</b> ({player['position']})<br>Readiness: {player['readiness_score']:.1f}%</p></div>", unsafe_allow_html=True)

    # Display unavailable players
    st.markdown("<p class='medium-font'>Unavailable Players</p>", unsafe_allow_html=True)
    unavailable_players = [f"{player['player_name']} ({player['position']})" for player in squad_recommendations['unavailable']]
    st.markdown(f"<p class='small-font'>{', '.join(unavailable_players)}</p>", unsafe_allow_html=True)

    # Add explanation to the sidebar
    with st.sidebar:
        st.markdown("## How It Works:")
        st.markdown("""
        ✅ **Readiness Score**: Calculated based on recent recovery data, trends, and risk factors.
        
        🏃‍♂️ **Player Status**:
        - Optimal (75-100%): Full training & match
        - Ready (60-74%): Full match
        - Limited (45-59%): 60-70 minutes
        - Bench (30-44%): Substitute option
        - Rest (0-29%): Recovery recommended
        
        📊 **Team Overview**: Shows improving and declining player counts.
        
        🔄 **Squad Recommendations**: Suggests optimal starting XI and bench based on readiness scores and positions.
        """)

