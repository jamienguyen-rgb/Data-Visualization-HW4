import streamlit as st
#from PIL import Image

st.set_page_config(page_title="Narrative Viz HW4", layout="wide")

st.title("Premier League Performance in 2023-2024 and 2024-2025 Seasons")
#st.write(Image.open('images/seattle-weather.jpg'))
st.write("This project is meant to explore performance trends in the Premier League from\
         the 2023-2204 and 2024-2025 seasons.\n")
st.write(
    "To explore this visual data story, please navigate it through the pages in the sidebar:\n"
    "- **Central Narrative**: We begin by taking into account performance patterns across seasons.\n"
    "- **Exploration**: For a closer reader-driven exploration of the data, we provide interactive designs.\n"
    "- **Methodology**: We lay down some key details about our data and limitations to our analysis.\n"
)
st.info("Dataset: `PL-season-2324, PL-season-2425`")
