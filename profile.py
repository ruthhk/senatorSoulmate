import streamlit as st
import pandas as pd
import numpy as np 
from pathlib import Path

logoPic = "pics/hill logo.png"
st.logo(logoPic,  size="medium")

### Data Frames 
# drugPrices = pd.read_csv("senator dataset - lowerDrugPrices.csv")
# drugPrices = drugPrices.rename(columns={"score": "drugPrices"})
# abortion = pd.read_csv("senator dataset - abortionWithMedicare.csv")
# abortion = abortion.rename(columns={"score": "abortion"})
# fertility = pd.read_csv("senator dataset - fertilityAccess.csv")
# fertility = fertility.rename(columns={"score": "fertility"})
# ice = pd.read_csv("senator dataset - fundingForICE.csv")
# ice = ice.rename(columns={"score": "ice"})
# housing = pd.read_csv("senator dataset - increaseHousing.csv")
# housing = housing.rename(columns={"score": "housing"})
# minWage = pd.read_csv("senator dataset - raiseTheMinimumWage.csv")
# minWage = minWage.rename(columns={"score": "minWage"})
# israel = pd.read_csv("senator dataset - stopIsraelSupport.csv")
# israel = israel.rename(columns={"score": "israel"})
# voting = pd.read_csv("senator dataset - votePhotoID.csv")
# voting = voting.rename(columns={"score": "voting"})
# iran = pd.read_csv("senator dataset - warInIran.csv")
# iran = iran.rename(columns={"score": "iran"})
# energy = pd.read_csv("senator dataset - windSolarTaxCredit.csv")
# energy = energy.rename(columns={"score": "energy"})
# deficit = pd.read_csv("senator dataset - deficit.csv")
# deficit = deficit.rename(columns={"score": "deficit"})
# fentanyl = pd.read_csv("senator dataset - fentanyl.csv")
# fentanyl = fentanyl.rename(columns={"score": "fentanyl"})
# sanctions = pd.read_csv("senator dataset - sanctions.csv")
# sanctions = sanctions.rename(columns={"score": "sanctions"})
# shoplifting = pd.read_csv("senator dataset - shoplifting.csv")
# shoplifting = shoplifting.rename(columns={"score": "shoplifting"})
# df = drugPrices.merge(abortion, how = 'left', on = 'senator')
# df = df.merge(fertility, how = 'left', on = 'senator')
# df = df.merge(ice, how = 'left', on = 'senator')
# df = df.merge(housing, how = 'left', on = 'senator')
# df = df.merge(minWage, how = 'left', on = 'senator')
# df = df.merge(israel, how = 'left', on = 'senator')
# df = df.merge(voting, how = 'left', on = 'senator')
# df = df.merge(iran, how = 'left', on = 'senator')
# df = df.merge(energy, how = 'left', on = 'senator')
# df = df.merge(deficit, how = 'left', on = 'senator')
# df = df.merge(fentanyl, how = 'left', on = 'senator')
# df = df.merge(sanctions, how = 'left', on = 'senator')
# df = df.merge(shoplifting, how = 'left', on = 'senator')
# df = df.set_index("senator", drop=True).rename_axis(None)
# df = df.replace(-1, 0)
# df.to_csv('cleanSenators.csv')


df = pd.read_csv(Path(__file__).parent / 'cleanSenators.csv')
df = df.set_index("senator", drop=False).rename_axis(None)


st.title("Fill out your profile")
st.markdown(
    """ 
    Tell us a little bit about where you're from and what you're looking for in a senator. 
    """
)

yourState = st.selectbox(
    "What state are you from?",
    ("AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
     "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
     "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
     "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
     "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"),
    index=None,
    placeholder="Select your state...",
)
yourState

with st.form("my_form"):
   st.write("In this quiz, you'll be asked to agree or disagree with a " \
   "statement. We'll calculate which senators you align most closely " \
   "with based on your answers.")
   drugPrices = st.pills("1. I support lowering medicaid prescription drug prices.", 
                     ("Agree", "Disagree"), selection_mode="single", required = True)
   abortion = st.pills("2. I support protecting abortion access.", 
                    ("Agree", "Disagree"), selection_mode = "single", required = True)
   fertility = st.pills("3. I support protecting access to fertility treatments like IVF", 
                    ("Agree", "Disagree"), selection_mode = "single", required = True)
   ice = st.pills("4. I support lowered levels of funding for ICE.", 
                    ("Agree", "Disagree"), selection_mode = "single", required = True)
   housing = st.pills("5. I support increasing the affordable housing supply.", 
                    ("Agree", "Disagree"), selection_mode = "single", required = True)
   minWage = st.pills("6. I support raising the minimum wage.", 
                   ("Agree", "Disagree"), selection_mode = "single", required = True)
   israel = st.pills("7. I support supplying weapons to Israel.", 
                  ("Agree", "Disagree"), selection_mode = "single", required = True)
   voting = st.pills("8. I support requiring photo ID to vote.", 
                  ("Agree", "Disagree"), selection_mode = "single", required = True)
   iran = st.pills("9. I support a war powers resolution to end the war in Iran.", 
                  ("Agree", "Disagree"), selection_mode = "single", required = True)
   energy = st.pills("10. I support tax credits and incentives for clean energy.", 
                  ("Agree", "Disagree"), selection_mode = "single", required = True)
   deficit = st.pills("11. I support a requirement to reduce the government spending " \
   "deficit in each fiscal budget.", 
                  ("Agree", "Disagree"), selection_mode = "single", required = True)
   fentanyl = st.pills("12. I support increasing prison time minimums for drugs like fentanyl.", 
                  ("Agree", "Disagree"), selection_mode = "single", required = True)
   sanctions = st.pills("13. I support expanding presidential sanction power to sanction Iran and Russia.", 
                  ("Agree", "Disagree"), selection_mode = "single", required = True)
   shoplifting = st.pills("14. I support requiring Homeland Security to detain undocumented " \
"immigrants arrested for crimes including shoplifting, larceny, and assault of an officer. ", 
                  ("Agree", "Disagree"), selection_mode = "single", required = True)
   submitted = st.form_submit_button('Find my senate soulmate', type="primary")

if (drugPrices == None or abortion == None or fertility == None 
    or minWage == None or housing == None or ice == None or 
    israel == None or voting == None or iran == None or energy == None or 
    deficit == None or fentanyl == None or sanctions == None or 
    sanctions == None or shoplifting == None or yourState == None): 
    if submitted == False: 
        # none :) 
        st.write("")
    if submitted == True: 
        st.write( "Oops! Looks like you didn't answer all the questions - try again!")
else: 
    drugPrices = 1 if drugPrices == "Agree" else 0
    abortion = 1 if abortion == "Agree" else 0
    fertility = 1 if fertility == "Agree" else 0
    minWage = 1 if minWage == "Agree" else 0
    housing = 1 if housing == "Agree" else 0
    ice = 0 if ice == "Agree" else 1
    israel = 0 if israel == "Agree" else 1
    voting = 1 if voting == "Agree" else 0
    iran = 1 if iran == "Agree" else 0
    energy = 1 if energy == "Agree" else 0
    deficit = 1 if deficit == "Agree" else 0
    fentanyl = 1 if fentanyl == "Agree" else 0
    sanctions = 1 if sanctions == "Agree" else 0
    shoplifting = 1 if shoplifting == "Agree" else 0

    playList = [drugPrices, abortion, fertility, ice, housing, minWage, israel, voting,
                iran, energy, deficit, fentanyl, sanctions, shoplifting]

    newdf = df.copy()

    columns = [
        "drugPrices", "abortion", "fertility", "ice",
        "housing", "minWage", "israel", "voting",
        "iran", "energy", "deficit", "fentanyl",
        "sanctions", "shoplifting"
    ]

    uniqueRow = newdf.index.values.tolist()

    for currRow in uniqueRow:
        for i, col in enumerate(columns):
            newdf.loc[currRow, col] = int(
                newdf.loc[currRow][col] == playList[i]
            )

    newdf["sums"] = newdf[columns].sum(axis=1)
    newdf = newdf.sort_values(by=["sums"], ascending=False)

    ID = newdf["sums"].max()
    matchperc = ID/14
    matchperc = round(matchperc, 4)
    displaydf = newdf.copy()
    displaydf = displaydf.drop(columns=["drugPrices", "abortion", "fertility", "ice",
            "housing", "minWage", "israel", "voting",
            "iran", "energy", "deficit", "fentanyl",
            "sanctions", "shoplifting"])
    displaydf.index.name = "Senators"
    displaydf["sums"]= round(displaydf["sums"]/.14, 2)
    displaydf["Match Percentage"] = displaydf["sums"].astype(str) + "%"
    displaydf = displaydf.drop(columns=["sums"])

    senatorMatches = newdf.loc[newdf["sums"] == ID]
    output = senatorMatches.index.values.tolist()

    stateMatches = newdf.copy()
    stateMatches = stateMatches.loc[stateMatches.index.astype(str).str.endswith(f"-{yourState})")]
    stateMatches["sums"] = stateMatches[columns].sum(axis=1)    
    leng = len(output)   

    profilesdf = pd.read_csv("senateDatingProfiles.csv")
    st.write("newdf columns:", newdf.columns.tolist())
    st.write("profilesdf columns:", profilesdf.columns.tolist())

    st.write("newdf preview:", newdf.head())
    st.write("profilesdf preview:", profilesdf.head())

    newdf = newdf.merge(profilesdf, how = "left", on = "senator")
    st.write("merged df", newdf)


    st.session_state["yourState"] = yourState
    st.session_state["senatorMatches"] = output
    st.session_state["matchperc"] = matchperc
    st.session_state["newdf"] = newdf

    st.switch_page("swiping.py")



