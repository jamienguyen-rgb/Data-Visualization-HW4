import streamlit as st
from utils.io import (load_points, load_wins)
from charts.charts import dashboard

st.set_page_config(page_title="Explore", layout="wide")
points_df = load_points()
win_df = load_wins()

st.title("Interactive Exploratory View")
st.write("Use interaction to validate and extend the story—select one team, then see their performance over each season.")

st.altair_chart(dashboard(points_df, wins_df), use_container_width=True)

st.markdown("**Guided prompts:**")
st.write("- Select one team (e.g., `Arsenal`, `Man United`)—how does their performance vary across seasons?")
st.write("- Select one team—how far apart are their points? What's the difference between their performances in each season?")
st.write("- Select one team-how does the difference in their points between seasons relate to their cumulative weekly wins between seasons?")
