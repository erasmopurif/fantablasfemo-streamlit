import streamlit as st

class MultiPage:
    def __init__(self):
        self.pages = []

    def add_page(self, title, func):
        '''
        :param str title: the title of page
        :param func func: Python function to render this page 
        '''
        self.pages.append({
            "title": title,
            "function": func
        })

    def run(self):
        # Dropsown to select the page from sidebar
        page = st.sidebar.selectbox(
            "Menu",
            self.pages,
            format_func = lambda page: page["title"]
        )

        # Run the app
        page["function"]()