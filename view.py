import streamlit as st
from app import predictSurvival

st.title("Know if you will survive titanic")

# name,pcl,sex,age ,sibsp, parch,fare,embarked

name = st.text_input("Enter your name")
age = st.text_input("Enter your age")
sex = st.radio("Select your gender", ["Male", "Female"])

pcl = st.radio("Your Public Status", ["High Class", "Middle Class", "Low Class"])

sibsp = st.text_input("Number of Siblings or Spouses onboard")
parch = st.text_input("Number of parents or children onboard")

fare = st.text_input("Your Fare for the Ticket")

embarked = st.radio("Where did you Onboard", ["Cherbourg", "Queenstown", "Southampton"])


if st.button("Predict"):
    
   pcl = 1 if pcl == "High Class" else 2 if pcl == "Middle Class" else 3

   sex = 0 if sex == "Male" else 1 

   embarked = 1 if embarked == "Cherbourg" else 2 if pcl == "Queenstown" else 0


   prediction = predictSurvival(sex, pcl, int(age), int(sibsp), int(parch), int(fare), embarked)
   if prediction == 0:
    st.markdown("<h1 style='color: red;'>You wouldnt survive Titanic 💀</h1>", unsafe_allow_html=True)
   else:
    st.markdown("<h1 style='color: green;'>You would survive Titanic 🥳</h1>", unsafe_allow_html=True)
