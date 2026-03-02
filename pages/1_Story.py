import streamlit as st
import altair as alt
from utils.io import load_data
from charts.charts import (
    base_theme,
    point_diff_chart,
    wins_line_promoted,
    points_line,
)

st.set_page_config(page_title="Story", layout="wide")

alt.themes.register("project", base_theme)
alt.themes.enable("project")

points_df = load_points()
wins_df = load_wins()

st.title("A Data Story: Premier League Performance Pattern")
st.markdown("**Central question:** *What patterns show up in Premier League performance across seasons?*")


st.header("1) Points Between Seasons")
st.write("First, we look at the general trend between 2023-2024 and 2024-2025 performance (points)")
st.altair_chart(points_line(points_df), use_container_width=True)
st.caption("Takeaway: This allows readers to get a general sense of the points trend of teams between seasons. There seems to be some positive  correlation between 2023-2024 and 2024-2025 performance. Liverpool, Arsenal, and Man City seem to have dominated both seasons.")

st.header("2) Point Differences from 2023-2024 to 2024-2025 Season")
st.write("We start with a bar chart to see changes in team performance (points) between seasons.")
st.altair_chart(point_diff_chart(points_df), use_container_width=True)
st.caption("Takeaway: Some teams that did the best in the 2024-2025 seasons actually have fewer points than they did in the 2023-2024 seasons. The middle-performing teams seem to generally improved from the previous season, especially Nottingham Forest. Teams that did the worse in 2024-2025 tend to have a seen a points decrease from the previous season. This indicates that improvement or lack of improvement from the previous season cannot predict future performance.")

st.header("3) Promoted Teams")
st.write("Changes in team performance can only be measured for teams that have remained in the Premier League for two consecutive seasons. What does performance look like for recently promoted teams?")
st.altair_chart(wins_line_promoted(wins_df), use_container_width=True)
st.caption("Takeaway: As expected, teams that are recently promoted tend to perform worse than teams that remained in the Premier League. The average cumulative wins (per week and in total) for non-promoted teams is much larger than that of promoted teams.")

