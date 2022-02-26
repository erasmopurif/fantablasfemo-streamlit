import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

from utils import get_team_dicts


def app():
    st.header("Costi di riconferma")

    # Init procedure
    ROSE_URL = "https://leghe.fantacalcio.it/fantablasfemo/area-gioco/rose"
    rose_res = requests.get(ROSE_URL)
    rose_html = BeautifulSoup(rose_res.text, "html.parser")

    teams_html = rose_html.find_all("li", {"class": "list-rosters-item"})

    teams = get_team_dicts(teams_html)
    teams_list = [k for k in teams]

    team_select = st.selectbox(
        "Squadra",
        teams_list
    )

    df_team = pd.DataFrame(teams[team_select]["roster_table"])
    df_team.columns = ["Ruolo", "Giocatore", "Club", "Quot.", "Conferma"]

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

    # role, name, club, cost, confirm = st.columns(5)

    # with role:
    #     st.caption("Ruolo")
    # with name:
    #     st.caption("Calciatore")
    # with club:
    #     st.caption("Club")
    # with cost:
    #     st.caption("Quotazione")
    # with confirm:
    #     st.caption("Riconferma")


    # roster = teams[team_select]["roster"]
    # p_total_cost = 0
    # p_total_confirm = 0
    # for player in roster:
    #     with role:
    #         st.write(roster[player]["role"])
    #     with name:
    #         # keep_player = st.checkbox(player, key=player)
    #         st.write(player)
    #     with club:
    #         st.write(roster[player]["club"])
    #     with cost:
    #         p_cost = roster[player]["cost"]
    #         p_total_cost += p_cost
    #         st.write(str(p_cost))
    #     with confirm:
    #         p_confirm = roster[player]["confirm"]
    #         p_total_confirm += p_confirm
    #         st.write(str(p_confirm))
        
    #     # if keep_player:
    #     #     p_total_confirm += p_confirm
    #     # else:
    #     #     p_total_cost += p_cost


    # _, _, _, total_cost, total_confirm = st.columns(5)

    # with total_cost:
    #     st.caption("Valore squadra")
    #     st.write(str(p_total_cost))

    # with total_confirm:
    #     st.caption("Totale riconferma")
    #     st.write(str(p_total_confirm))