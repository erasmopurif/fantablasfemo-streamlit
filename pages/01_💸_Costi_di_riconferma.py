import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

from utils import get_team_dicts, compute_gain_confirm

# Page Config
st.set_page_config(
    page_title="Costi di riconferma",
    page_icon="⚽️"
)

st.header("Costi di riconferma")

# Init procedure
ROSE_URL = "https://leghe.fantacalcio.it/fantablasfemo/area-gioco/rose"
rose_res = requests.get(ROSE_URL)
rose_html = BeautifulSoup(rose_res.text, "html.parser")
teams_html = rose_html.find_all("li", {"class": "list-rosters-item"})

try:
    PLAYER_LIST_URL = "https://drive.google.com/file/d/1PVfvHppknf512c6CmdMLnsdfF9-g5UNV/view?usp=sharing"
    PLAYER_LIST_URL = "https://drive.google.com/uc?id=" + PLAYER_LIST_URL.split('/')[-2]
    df_players = pd.read_csv(PLAYER_LIST_URL, header=None)
except:
    df_players = None

teams = get_team_dicts(teams_html, df_players)
teams_list = [k for k in teams]

team_select = st.selectbox(
    "Squadra",
    teams_list
)

roster = teams[team_select]["roster_table"]
df_team = pd.DataFrame(roster, columns=["role", "name", "club", "cost", "confirm"])
player_names = df_team["name"]

df_team.columns = ["Ruolo", "Giocatore", "Club", "Quot.", "Conf."]

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

selected_players = st.multiselect("Seleziona i giocatori da riconfermare:", player_names)

compute_costs = st.button("Calcola costi")
if compute_costs:
    st.caption("Calciatori confermati")
    st.info(", ".join(selected_players))
    total_gain, total_confirm =  compute_gain_confirm(roster, selected_players)
    st.caption("Crediti di partenza")
    base_coins = teams[team_select]["res_coins"]
    st.write(str(base_coins))
    st.caption("Crediti incassati cessioni")
    st.write(str(total_gain))
    st.caption("Costo riconferme")
    st.write(str(total_confirm))
    res_coins = (int(base_coins) + total_gain) - total_confirm
    st.caption("Crediti residui finali")
    st.write(str(res_coins))

