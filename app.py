import streamlit as st

home = st.Page("homePage.py", title="Home", default=True)
profile = st.Page("profile.py", title="Create your Profile")
swiping = st.Page("swiping.py", title ="Start Swiping")
endpage = st.Page("endpage.py", title = "Your Results")
onlySwipes = st.Page("onlySwipes.py", title = "Start Swiping")

pg = st.navigation([home, profile, swiping, endpage, onlySwipes], position="hidden")

pg.run()
