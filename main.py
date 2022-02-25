import streamlit as st
import requests
from bs4 import BeautifulSoup

from multipage import MultiPage
from pages import confirm_costs
from utils import get_team_dicts


# Instance of the app
app = MultiPage()

# Title of the main page
st.title("FANTABLASFEMO")


# Add apps (pages)
app.add_page("Costi di riconferma", confirm_costs.app)


# Run main app
app.run()