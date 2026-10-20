import streamlit as st 
import pandas as pd
from pathlib import Path


logoPic = "pics/hillLogo.png"
st.logo(logoPic,  size="medium")

yourState = st.session_state.get("yourState")
senatorMatches = st.session_state.get("senatorMatches", [])
matchperc = st.session_state.get("matchperc")
newdf = pd.DataFrame(st.session_state.get("newdf"))
matchList = st.session_state.get("matchList")
swipeOptions = st.session_state.get("swipeOptions")

st.title("Your matches", text_alignment="center", anchor=False)


for currSenator in matchList:
    fullName = swipeOptions.loc[
        swipeOptions["senator"] == currSenator,
        "full name"
        ].iloc[0]
    messageMeLink = swipeOptions.loc[
        swipeOptions["senator"] == currSenator,
        "contact"
        ].iloc[0]
    bios = swipeOptions.loc[
            swipeOptions["senator"] == currSenator,
            "Bios"
            ].iloc[0]
    with st.container(border=True): 
        col1, col2 = st.columns([1,2], border=False)
        with col1: 
            st.image(f"pics/{currSenator}.jpg", width = "stretch")
        with col2: 
            st.subheader(fullName, text_alignment="left", anchor = False)
            st.write(bios)
            st.link_button("dm me", icon = "💬", url = messageMeLink)

