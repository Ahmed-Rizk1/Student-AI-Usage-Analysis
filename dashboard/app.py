
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Set page config
st.set_page_config(layout="wide", page_title="Student AI Usage Dashboard")

# Load data
@st.cache_data
def load_data():
    path = os.path.join("data", "processed", "cleaned_data.csv")
    if not os.path.exists(path):
        st.error("Data file not found. Please run src/cleaning.py first.")
        return None
    return pd.read_csv(path)

df = load_data()

if df is not None:
    # Sidebar
    st.sidebar.header("Filters")
    
    # Filter by AI Usage
    usage_filter = st.sidebar.multiselect(
        "AI User Status",
        options=df["user_category"].unique(),
        default=df["user_category"].unique()
    )
    
    # Filter by Tool
    # Handle None/NaN for tool selection
    tools = df[df["ai_tools_used"] != "None"]["ai_tools_used"].unique().tolist()
    tool_filter = st.sidebar.multiselect(
        "AI Tool Used",
        options=tools,
        default=tools
    )
    
    # Apply filters
    # If "None" is in usage status (Non-User), we should include rows where ai_tools_used is None
    # Complexity: Filter logic needs to be robust
    
    # Simplified filter: just filter by user category first
    df_filtered = df[df["user_category"].isin(usage_filter)]
    
    # Then detailed filter for AI tools if applicable
    # We create a mask: row is kept if it's a Non-User OR if it uses one of the selected tools
    mask_tool = (df_filtered["ai_tools_used"].isin(tool_filter)) | (df_filtered["user_category"] == "Non-User")
    df_filtered = df_filtered[mask_tool]

    # Main Dashboard
    st.title("📊 Student AI Usage Analysis")
    st.markdown("Insights into how AI tools impact student performance.")

    # KPI Section
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Students", len(df_filtered))
    with col2:
        avg_grade_after = df_filtered["grades_after_ai"].mean()
        st.metric("Avg Grade (Current)", f"{avg_grade_after:.1f}")
    with col3:
        avg_improvement = df_filtered["grade_improvement"].mean()
        st.metric("Avg Grade Improvement", f"{avg_improvement:.1f}")
    with col4:
        avg_study = df_filtered["study_hours_per_day"].mean()
        st.metric("Avg Study Hours/Day", f"{avg_study:.1f}")

    # Charts
    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("Grades: Before vs After AI")
        # Comparison of distributions
        fig_grades = go.Figure()
        fig_grades.add_trace(go.Box(y=df_filtered["grades_before_ai"], name="Before AI"))
        fig_grades.add_trace(go.Box(y=df_filtered["grades_after_ai"], name="After AI"))
        fig_grades.update_layout(height=400)
        st.plotly_chart(fig_grades, use_container_width=True)
        
    with c2:
        st.subheader("AI Tool Popularity")
        tool_counts = df_filtered[df_filtered["ai_tools_used"] != "None"]["ai_tools_used"].value_counts().reset_index()
        tool_counts.columns = ["Tool", "Count"]
        fig_tools = px.bar(tool_counts, x="Tool", y="Count", color="Tool")
        st.plotly_chart(fig_tools, use_container_width=True)

    c3, c4 = st.columns(2)
    
    with c3:
        st.subheader("Study Hours vs Grade Improvement")
        fig_scatter = px.scatter(
            df_filtered, 
            x="study_hours_per_day", 
            y="grade_improvement",
            color="user_category",
            size="daily_screen_time_hours",
            hover_data=["ai_tools_used", "purpose_of_ai"]
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
        
    with c4:
        st.subheader("Usage Purpose Distribution")
        purpose_counts = df_filtered[df_filtered["purpose_of_ai"] != "None"]["purpose_of_ai"].value_counts()
        fig_pie = px.pie(values=purpose_counts.values, names=purpose_counts.index)
        st.plotly_chart(fig_pie, use_container_width=True)
