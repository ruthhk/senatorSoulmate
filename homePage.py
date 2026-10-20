import streamlit as st
from pathlib import Path

logoPic = "pics/hillLogo.png"
st.logo(logoPic,  size="medium")

st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }

        [data-testid="stSidebarCollapsedControl"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

def write_right(text):
    st.markdown(f"<div style='text-align: right'>{text}</div>", unsafe_allow_html=True)


bigLogo = "pics/hillLogoBig.png"
capHill = "pics/capitolHill.png"
ted = "pics/tedCruz.png"

with st.container(horizontal_alignment="center"): 
    st.image(capHill, width="stretch")

st.divider()
# st.title("Find your perfect match",
#          text_alignment="center", anchor=False)

leftcol, rightcol = st.columns([1,1], border = False, vertical_alignment="bottom")
st.space("small")
leftcol1, rightcol1 = st.columns([1,1], border = False, vertical_alignment="bottom")
st.space("small")
leftcol2, rightcol2 = st.columns([1,1], border = False, vertical_alignment="bottom")
st.space("small")
leftcol3, rightcol3 = st.columns([1,1], border = False, vertical_alignment="bottom")
st.space("small")

with st.container():
    with leftcol: 
        st.image("pics/alsobrooks.png", width="stretch")
    with rightcol: 
        with st.container(horizontal_alignment="right"):
            st.subheader("We're political scientists.",anchor = False, text_alignment="right")
            write_right("Our Hill Labs researchers, behavioral analysts, "
            "and matchmakers study senators and compatibility " 
            "so we can make Hill better for you. We've gotten pretty good at it.")
            st.space("xxsmall")





with leftcol1: 
    st.subheader("Find a match in this crazy system.", anchor=False)
    st.write("It's hard to find politicians you actually like - we made it easier.")
with rightcol1: 
    st.image("pics/moody.png", width = "stretch")
    


with leftcol2: 
    st.image("pics/jonOssoff.png", width = "stretch")
with rightcol2: 
    with st.container(horizontal_alignment="right"):
        st.subheader("How it works.", anchor=False, text_alignment="right")
        write_right("Create a profile. We'll take your profile and offer senators" \
        " who agree with you at least 70% of the time. Swipe through your options " \
        "to find a match.")
        st.space("xxsmall")


with leftcol3: 
    st.subheader("Don't want a profile?")
    st.write("No profile? No problem. Experience a limited version of Hill and" \
    " swipe through all 100 senators until you find one you like.")
    
with rightcol3: 
    st.image(ted, width="stretch")
st.divider()

st.space("medium")
rcol, lecol = st.columns([1,1], border = False)
with rcol: 
    with st.container(horizontal_alignment="center"):
        toProfile = st.button(label = "Create your profile", type="primary")
        if toProfile: 
            st.switch_page("profile.py")

with lecol:
    with st.container(horizontal_alignment="center"):
        toSwipe = st.button(label = "Just swipe", type="primary")
        if toSwipe: 
            st.switch_page("onlySwipes.py")
