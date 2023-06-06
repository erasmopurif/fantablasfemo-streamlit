import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

from utils import get_team_dicts

# Page config
st.set_page_config(
    page_title="FVM",
    page_icon="⚽️"
)

st.header("Fanta Valore di Mercato")

# Init procedure
ROSE_URL = "https://leghe.fantacalcio.it/fantablasfemo/area-gioco/rose"
rose_res = requests.get(ROSE_URL)
rose_html = BeautifulSoup(rose_res.text, "html.parser")
teams_html = rose_html.find_all("li", {"class": "list-rosters-item"})

PLAYER_LIST_URL = "https://drive.google.com/file/d/1PVfvHppknf512c6CmdMLnsdfF9-g5UNV/view?usp=sharing"
PLAYER_LIST_URL = "https://drive.google.com/uc?id=" + PLAYER_LIST_URL.split('/')[-2]
df_players = pd.read_csv(PLAYER_LIST_URL, header=None)

teams = get_team_dicts(teams_html, df_players)
teams_list = [k for k in teams]

team_select = st.selectbox(
    "Squadra",
    teams_list
)

roster = teams[team_select]["roster_table"]
df_team = pd.DataFrame(roster, columns=["role", "name", "club", "cost", "fvm-1000", "fvm-300"])
player_names = df_team["name"]

df_team.columns = ["Ruolo", "Giocatore", "Club", "Quot.", "FVM/1000", "FVM/300"]

# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

st.table(df_team)