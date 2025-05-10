import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page configuration
st.set_page_config(
    page_title="Rohit Sharma Test Career Analysis",
    page_icon="🏏",
    layout="wide"
)

# Add custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #0D47A1;
        margin-top: 1rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        border-radius: 5px;
        padding: 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .highlight {
        color: #D32F2F;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='main-header'>Rohit Sharma's Test Cricket Career Analysis</h1>", unsafe_allow_html=True)

# Create dataframes from Rohit Sharma's Test career data
# Phase-wise Performance
phase_data = pd.DataFrame({
    'Phase': ['2013-2016', '2017-2019', '2020-2022', '2023-2024'],
    'Matches': [18, 14, 15, 11],
    'Innings': [32, 25, 26, 19],
    'Runs': [1184, 1276, 1045, 632],
    'Average': [39.47, 55.48, 41.80, 36.73],
    'Strike Rate': [49.87, 62.73, 54.42, 58.91],
    '50s': [3, 5, 5, 3],
    '100s': [3, 5, 2, 2]
})

# Position-wise Performance
position_data = pd.DataFrame({
    'Position': ['Opening', '#3', '#5', '#6'],
    'Innings': [58, 2, 25, 17],
    'Runs': [2773, 52, 996, 316],
    'Average': [49.52, 26.00, 43.30, 19.75],
    'Strike Rate': [58.37, 42.98, 53.65, 45.92],
    '50s': [10, 0, 4, 2],
    '100s': [9, 0, 2, 1]
})

# Home vs Away Analysis
venue_data = pd.DataFrame({
    'Venue': ['Home', 'Away'],
    'Matches': [33, 25],
    'Innings': [57, 45],
    'Runs': [2692, 1445],
    'Average': [50.79, 35.24],
    'Strike Rate': [58.91, 51.54],
    '50s': [9, 7],
    '100s': [9, 3]
})

# Opposition-wise Performance
opposition_data = pd.DataFrame({
    'Opposition': ['Australia', 'Bangladesh', 'England', 'New Zealand', 'South Africa', 'Sri Lanka', 'West Indies'],
    'Matches': [12, 6, 15, 5, 9, 6, 5],
    'Innings': [23, 9, 27, 9, 16, 10, 8],
    'Runs': [708, 679, 927, 474, 714, 386, 249],
    'Average': [35.40, 97.00, 38.63, 59.25, 47.60, 38.60, 31.13],
    'High Score': [120, 212, 161, 176, 212, 102, 177],
    '50s': [2, 2, 3, 2, 2, 3, 2],
    '100s': [1, 2, 3, 2, 2, 1, 1]
})

# Match Situation Performance
situation_data = pd.DataFrame({
    'Situation': ['1st innings', '2nd innings', '3rd innings', '4th innings'],
    'Innings': [49, 29, 17, 7],
    'Runs': [2487, 834, 663, 153],
    'Average': [52.91, 29.79, 44.20, 25.50],
    'Strike Rate': [57.38, 54.16, 55.72, 51.00],
    '50s': [8, 5, 3, 0],
    '100s': [9, 1, 2, 0]
})

# Dismissal Analysis
dismissal_data = pd.DataFrame({
    'Dismissal Type': ['Caught', 'Bowled', 'LBW', 'Run Out', 'Stumped'],
    'Count': [63, 14, 18, 3, 2],
    'Percentage': [63.0, 14.0, 18.0, 3.0, 2.0],
    'Average Runs': [43.86, 31.21, 39.17, 37.33, 22.50]
})

# Shot Distribution Analysis
shot_data = pd.DataFrame({
    'Shot Type': ['Defensive Stroke', 'Front Foot Drive', 'Flick/Glance', 'Cut', 
                 'Pull/Hook', 'Square Drive', 'Sweep/Reverse Sweep', 'Lofted Drive'],
    'Frequency (%)': [29.6, 19.8, 12.4, 11.9, 9.7, 7.6, 5.3, 3.7],
    'Runs Scored': [342, 1142, 723, 692, 587, 423, 287, 258],
    'Average': [0, 47.58, 48.20, 49.43, 41.93, 42.30, 35.88, 32.25],
    'Dismissal Rate (%)': [1.8, 8.7, 6.4, 5.9, 7.2, 6.8, 9.1, 12.4]
})

# Career overview in top row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Test Matches", "58", "2013-Present")
with col2:
    st.metric("Total Runs", "4,137", "Avg: 44.96")
with col3:
    st.metric("Centuries", "12", "+16 Half-centuries")
with col4:
    st.metric("Captaincy", "15 matches", "Win %: 66.67")

# Career phases and timeline
st.markdown("<h2 class='sub-header'>Career Evolution</h2>", unsafe_allow_html=True)
chart_col1, chart_col2 = st.columns([2, 1])

with chart_col1:
    # Interactive line chart showing performance evolution
    phase_metrics = st.selectbox(
        "Select metrics to view career evolution:",
        ["Average & Strike Rate", "Runs per Phase", "Centuries & Half-centuries"]
    )
    
    if phase_metrics == "Average & Strike Rate":
        fig = px.line(phase_data, x='Phase', y=['Average', 'Strike Rate'], 
                      title="Performance Over Career Phases", markers=True,
                      color_discrete_sequence=['#1E88E5', '#FFC107'])
        st.plotly_chart(fig, use_container_width=True)
    elif phase_metrics == "Runs per Phase":
        fig = px.bar(phase_data, x='Phase', y='Runs', 
                     title="Runs Scored in Different Career Phases", 
                     color='Phase', text_auto=True)
        st.plotly_chart(fig, use_container_width=True)
    else:
        fig = px.bar(phase_data, x='Phase', y=['50s', '100s'], barmode='group',
                    title="50s and 100s Across Career", 
                    color_discrete_sequence=['#FFC107', '#D32F2F'])
        st.plotly_chart(fig, use_container_width=True)

with chart_col2:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.markdown("### Key Insights")
    st.markdown("- **Peak Performance**: 2017-2019 with average of 55.48")
    st.markdown("- **Consistent Phase**: 2020-2022 maintaining 41.80 average")
    st.markdown("- **Recent Form**: Slight decline to 36.73 in 2023-2024")
    st.markdown("- **Career Transformation**: Moved to opening in 2019")
    st.markdown("</div>", unsafe_allow_html=True)

# Batting position analysis
st.markdown("<h2 class='sub-header'>Performance by Batting Position</h2>", unsafe_allow_html=True)
pos_col1, pos_col2 = st.columns([3, 1])

with pos_col1:
    position_metric = st.radio(
        "Select metric to analyze by position:",
        ["Average", "Runs", "Strike Rate", "Centuries"],
        horizontal=True
    )
    
    if position_metric == "Centuries":
        fig = px.bar(position_data, x='Position', y='100s', 
                     title="Centuries by Batting Position", color='Position',
                     text_auto=True)
    else:
        fig = px.bar(position_data, x='Position', y=position_metric, 
                     title=f"{position_metric} by Batting Position", color='Position',
                     text_auto='.1f' if position_metric in ["Average", "Strike Rate"] else True)
    st.plotly_chart(fig, use_container_width=True)

with pos_col2:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.markdown("### Position Impact")
    st.markdown("- <span class='highlight'>49.52</span> average as opener (58 innings)", unsafe_allow_html=True)
    st.markdown("- <span class='highlight'>43.30</span> average at #5 (25 innings)", unsafe_allow_html=True)
    st.markdown("- <span class='highlight'>75%</span> of centuries scored as opener", unsafe_allow_html=True)
    st.markdown("- Position change in 2019 revolutionized his Test career")
    st.markdown("</div>", unsafe_allow_html=True)

# Two analysis sections side by side
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h2 class='sub-header'>Home vs Away Performance</h2>", unsafe_allow_html=True)
    venue_view = st.selectbox(
        "Select home vs away comparison type:",
        ["Average Comparison", "Runs Distribution", "Centuries Comparison"]
    )
    
    if venue_view == "Average Comparison":
        fig = px.bar(venue_data, x='Venue', y='Average', color='Venue',
                    title="Batting Average: Home vs Away", text_auto='.2f')
    elif venue_view == "Runs Distribution":
        fig = px.pie(venue_data, values='Runs', names='Venue',
                    title="Runs Distribution: Home vs Away")
    else:
        fig = px.bar(venue_data, x='Venue', y=['50s', '100s'], barmode='group',
                    title="Centuries & Half-centuries: Home vs Away",
                    color_discrete_sequence=['#FFC107', '#D32F2F'])
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("<h2 class='sub-header'>Performance by Match Situation</h2>", unsafe_allow_html=True)
    innings_view = st.selectbox(
        "Select innings analysis view:",
        ["Average by Innings", "Total Runs by Innings", "Conversion Rate"]
    )
    
    if innings_view == "Average by Innings":
        fig = px.bar(situation_data, x='Situation', y='Average', color='Situation',
                    title="Average in Different Innings", text_auto='.2f')
    elif innings_view == "Total Runs by Innings":
        fig = px.bar(situation_data, x='Situation', y='Runs', color='Situation',
                    title="Runs in Different Innings", text_auto=True)
    else:
        # Calculate conversion rate (100s/(50s+100s))
        situation_data['Conversion Rate'] = situation_data['100s'] / (situation_data['50s'] + situation_data['100s']) * 100
        fig = px.bar(situation_data, x='Situation', y='Conversion Rate', color='Situation',
                    title="Conversion Rate by Innings", text_auto='.1f')
    st.plotly_chart(fig, use_container_width=True)

# Opposition Analysis
st.markdown("<h2 class='sub-header'>Performance Against Different Teams</h2>", unsafe_allow_html=True)

opposition_metric = st.selectbox(
    "Select metric to analyze by opposition:",
    ["Average", "Total Runs", "Centuries & Half-centuries", "High Score"]
)

if opposition_metric == "Average":
    # Sort by average
    sorted_data = opposition_data.sort_values(by='Average', ascending=False)
    fig = px.bar(sorted_data, x='Opposition', y='Average', color='Opposition',
                title="Batting Average Against Different Teams", text_auto='.2f')
    st.plotly_chart(fig, use_container_width=True)
elif opposition_metric == "Total Runs":
    # Sort by runs
    sorted_data = opposition_data.sort_values(by='Runs', ascending=False)
    fig = px.bar(sorted_data, x='Opposition', y='Runs', color='Opposition',
                title="Total Runs Against Different Teams", text_auto=True)
    st.plotly_chart(fig, use_container_width=True)
elif opposition_metric == "High Score":
    # Sort by high score
    sorted_data = opposition_data.sort_values(by='High Score', ascending=False)
    fig = px.bar(sorted_data, x='Opposition', y='High Score', color='Opposition',
                title="Highest Score Against Different Teams", text_auto=True)
    st.plotly_chart(fig, use_container_width=True)
else:
    # Create a grouped bar for 50s and 100s
    fig = px.bar(opposition_data, x='Opposition', y=['50s', '100s'], barmode='group',
                title="Centuries & Half-centuries by Opposition",
                color_discrete_sequence=['#FFC107', '#D32F2F'])
    st.plotly_chart(fig, use_container_width=True)

# Technical Analysis section
st.markdown("<h2 class='sub-header'>Technical Analysis</h2>", unsafe_allow_html=True)
tech_col1, tech_col2 = st.columns(2)

with tech_col1:
    st.markdown("<h3>Dismissal Analysis</h3>", unsafe_allow_html=True)
    fig = px.pie(dismissal_data, values='Count', names='Dismissal Type',
                title="How Rohit Gets Out", hole=0.4,
                color_discrete_sequence=px.colors.qualitative.Set3)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig, use_container_width=True)

with tech_col2:
    st.markdown("<h3>Shot Effectiveness</h3>", unsafe_allow_html=True)
    shot_metric = st.radio(
        "Select shot analysis metric:",
        ["Average per Shot", "Dismissal Rate", "Run Production"],
        horizontal=True
    )
    
    if shot_metric == "Average per Shot":
        # Filter out defensive strokes for average (they have 0 average)
        filtered_data = shot_data[shot_data['Shot Type'] != 'Defensive Stroke'].sort_values(by='Average', ascending=False)
        fig = px.bar(filtered_data, x='Shot Type', y='Average', color='Shot Type',
                    title="Batting Average by Shot Type", text_auto='.2f')
    elif shot_metric == "Dismissal Rate":
        sorted_data = shot_data.sort_values(by='Dismissal Rate (%)')
        fig = px.bar(sorted_data, x='Shot Type', y='Dismissal Rate (%)', color='Shot Type',
                    title="Dismissal Rate by Shot Type (%)", text_auto='.1f')
    else:
        sorted_data = shot_data.sort_values(by='Runs Scored', ascending=False)
        fig = px.bar(sorted_data, x='Shot Type', y='Runs Scored', color='Shot Type',
                    title="Runs Scored by Shot Type", text_auto=True)
    st.plotly_chart(fig, use_container_width=True)

# Add a key takeaways section
st.markdown("<h2 class='sub-header'>Key Takeaways</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.markdown("### Strengths")
    st.markdown("- Exceptional first innings player (avg 52.91)")
    st.markdown("- Dominant as opener (avg 49.52)")
    st.markdown("- Outstanding at home (avg 50.79)")
    st.markdown("- Exceptional against Bangladesh (avg 97.00)")
    st.markdown("- Cut shot most effective (avg 49.43)")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.markdown("### Challenges")
    st.markdown("- Away performance (avg 35.24)")
    st.markdown("- Fourth innings struggles (avg 25.50)")
    st.markdown("- Vulnerability to being caught (63%)")
    st.markdown("- Recent form decline (2023-24 avg 36.73)")
    st.markdown("- Struggles against Australia (avg 35.40)")
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.markdown("### Career Highlights")
    st.markdown("- Highest score: 212 vs South Africa")
    st.markdown("- Scored 100s against 7 different nations")
    st.markdown("- 66.67% win rate as captain")
    st.markdown("- 9 centuries as opener")
    st.markdown("- Peak phase: 2017-2019 (avg 55.48)")
    st.markdown("</div>", unsafe_allow_html=True)

# Footer with data source
st.markdown("---")
st.markdown("Data Source: Comprehensive Statistical Analysis of Rohit Sharma's Cricket Career: T20I and Test (As of October 2024)")
st.markdown("Dashboard created with Streamlit and Plotly")

# Instructions in sidebar for GitHub deployment
with st.sidebar:
    st.title("Dashboard Information")
    st.markdown("### Rohit Sharma Test Career Analysis")
    st.markdown("This dashboard provides an interactive analysis of Rohit Sharma's Test cricket career statistics from 2013 to 2024.")
    
    st.markdown("### GitHub Deployment Instructions")
    st.code("""
    # Steps to deploy on GitHub:
    1. Create a GitHub repository
    2. Upload this script as app.py
    3. Create requirements.txt with:
       streamlit
       pandas
       plotly
    4. Connect to Streamlit Cloud
    5. Deploy from your repository
    """)
    
    st.markdown("### About the Data")
    st.markdown("Data includes 58 Test matches spanning from Rohit's debut in 2013 through October 2024.")
