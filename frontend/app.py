import streamlit as st
from datetime import datetime

st.set_page_config (
    page_title = "NutriHome",
    page_icon = "🍕",
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "fullname" not in st.session_state:
    st.session_state.fullname = ""

if "dob" not in st.session_state:
    st.session_state.dob = datetime(2000, 1, 1)

if "weight" not in st.session_state:
    st.session_state.weight = 0

if "height" not in st.session_state:
    st.session_state.weight = 0

if "activity_level" not in st.session_state:
    st.session_state.activity_level = ""

if "avatar" not in st.session_state:
    st.session_state.avatar = ""

if "login_page" not in st.session_state:
    st.session_state.login_page = False

if "language" not in st.session_state:
    st.session_state.language = "Vietnamese"

def logout():
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.fullname = ""
        st.session_state.dob = datetime(2000, 1, 1)
        st.session_state.weight = 0
        st.session_state.height = 0
        st.session_state.activity_level = ""
        st.session_state.login_page = ""
        st.session_state.register = False
        st.rerun()

login_page = st.Page("pages/login.py", title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

home = st.Page("pages/home.py", title="Home", icon=":material/home:")

profile = st.Page("pages/personal/profile.py", title="Profile", icon=":material/account_circle:")
settings = st.Page("pages/personal/settings.py", title="Settings", icon=":material/bug_report:")

weeklyMenu = st.Page("pages/features/weeklyMenu.py", title="Weekly Menu", icon=":material/assignment:")
recipes = st.Page("pages/features/recipes.py", title="Recipes", icon=":material/content_paste_search:")
history = st.Page("pages/features/history.py", title="History", icon=":material/history:")
family_health = st.Page("pages/features/family_health.py", title="Family Health", icon=":material/diversity_1:")
community = st.Page("pages/features/community.py", title="Community", icon=":material/forum:")


if st.session_state.logged_in:
    pg = st.navigation(
        {
            "": [home],
            "Features": [weeklyMenu, recipes, history, family_health, community],
            "Personal": [profile, settings, logout_page],
        }
    )
else:
    pg = st.navigation([home])

    if st.session_state.login_page:
        pg = st.navigation([login_page])

pg.run()