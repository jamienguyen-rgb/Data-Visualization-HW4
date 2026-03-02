import streamlit as st

st.set_page_config(page_title="Methods", layout="wide")

st.title("Methods & Limitations")
st.write("- Data source: `PL-season-2324', 'PL-season-2425'")
st.write("- Variables used: `Date`, `HomeTeam`, `AwayTeam`, `FTR`")
st.subheader("Limitations")
st.write("- Two seasons; patterns don’t generalize to all other Premier League seasons.")
st.write("- Since our analysis is based on observational data; the relationships here are not causal.")
st.write("- This analysis assumes points and wins are the only metric for a season's success. For example, this analysis doesn't consider how dominant a team is based on the score of each game (a 1-0 win in the last few minutes or a 6-0 win).")
