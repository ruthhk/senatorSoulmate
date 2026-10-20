import streamlit as st
import pandas as pd
from pathlib import Path


logoPic = "pics/hillLogo.png"
st.logo(logoPic,  size="medium")

swipeOptions = pd.read_csv(Path(__file__).parent /'senateDatingProfiles.csv')
swipeOptions["Date of birth"] = pd.to_datetime(swipeOptions["Date of birth"])
today = pd.Timestamp.today()
swipeOptions["age"] = (
    today.year
    - swipeOptions["Date of birth"].dt.year
    - (
        (today.month < swipeOptions["Date of birth"].dt.month)
        | (
            (today.month == swipeOptions["Date of birth"].dt.month)
            & (today.day < swipeOptions["Date of birth"].dt.day)
        )
    ).astype(int)
)

uniqueSenator = swipeOptions["senator"].to_list()
matchNum = range(len(uniqueSenator))

col1, col2, col3 = st.columns([0.7, 2, 0.7], border=False)


if "senator_index" not in st.session_state:
    st.session_state.senator_index = 0

if "swipeOptions" not in st.session_state:
    st.session_state.swipeOptions = swipeOptions

if "matchList" not in st.session_state:
    st.session_state.matchList = []

if uniqueSenator:
    currIndex = st.session_state.senator_index
    with col2: 
        currSenator = uniqueSenator[currIndex]
        fullName = swipeOptions.loc[
            swipeOptions["senator"] == currSenator,
            "full name"
        ].iloc[0]
        age = swipeOptions.loc[
            swipeOptions["senator"] == currSenator,
            "age"
        ].iloc[0]
        party = swipeOptions.loc[
            swipeOptions["senator"] == currSenator,
            "Party"
        ].iloc[0] 
        bios = swipeOptions.loc[
            swipeOptions["senator"] == currSenator,
            "Bios"
        ].iloc[0]          
        st.header(fullName, text_alignment="center", anchor = False)
        st.progress(
            currIndex / len(uniqueSenator),
            text=f"Senator {currIndex + 1} of {len(uniqueSenator)}",
        )

        with st.container(border=False): 
            st.image(f"pics/{currSenator}.jpg", width = "stretch")
            leftSide, rightSide = st.columns([1,1], border=False)
            with leftSide:
                st.subheader(party, text_alignment="left", anchor=False)
            with rightSide: 
                st.subheader(age, text_alignment="right",anchor=False)

            badges = []


            if age >= 70:
                badges.append(":orange-badge[on the older side]")
            if age < 51:
                badges.append(":green-badge[super young]")
            badges.append(":green-badge[is a senator]")
            if badges:
                st.markdown(" ".join(badges))
            
            st.write(bios)






        if currIndex >= len(uniqueSenator) - 1: 
            with st.container(horizontal=True, horizontal_alignment= "center"): 
                colL, colR = st.columns([1,1], vertical_alignment="center")
                with colL:
                    with st.container(border=False):
                        if st.button("Dislike :x:", width="stretch"):
                            st.switch_page("endpage.py")
                
                with colR:
                    with st.container(border=False):
                        if st.button("Like :white_check_mark:", width="stretch"): 
                            st.session_state.matchList.append(currSenator)
                            st.switch_page("endpage.py")
        else:
            with st.container(horizontal=True, horizontal_alignment="center"):
                colL, colR = st.columns([1,1], vertical_alignment="center") 
                with colL:
                    with st.container(border=False):
                        if st.button("Dislike :x:", width="stretch"):
                            st.session_state.senator_index += 1
                            st.rerun()
                with colR:
                    with st.container(border=False):
                        if st.button("Like :white_check_mark:", width="stretch"): 
                            st.session_state.senator_index += 1
                            st.session_state.matchList.append(currSenator)
                            st.rerun()
                

else:
    st.write("You have no matches :cry:.")
