import streamlit as st
from io import load_data()
from charts import dashboard

st.set_page_config(page_title="Explore", layout="wide")
df = load_data()

st.title("Interactive Exploratory View")
st.write("Use interaction to validate and extend the story—select one team, then see their performance over each season.")

st.altair_chart(dashboard(df), use_container_width=True)

st.markdown("**Guided prompts:**")
st.write("- Select one team (e.g., `Arsenal`, `Man United`)—how does their performance vary across seasons?")
st.write("- Select one team—how far apart are their points? What's the difference between their performances in each season?")
st.write("- Select one team-how does the difference in their points between seasons relate to their cumulative weekly wins between seasons?")
