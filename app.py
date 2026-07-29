import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("titanic_model.pkl","rb"))

st.title("Titanic Survival Prediction")

pclass = st.selectbox("Passenger Class",[1,2,3])

sex = st.selectbox("Sex",["Male","Female"])

age = st.number_input("Age",0,100,25)

fare = st.number_input("Fare",0.0)

embarked = st.selectbox("Embarked",["C","Q","S"])

sibsp = st.number_input("Siblings/Spouse",0,10)

parch = st.number_input("Parents/Children",0,10)

sex_female = 1 if sex=="Female" else 0
sex_male = 1 if sex=="Male" else 0

embarked_C = 1 if embarked=="C" else 0
embarked_Q = 1 if embarked=="Q" else 0
embarked_S = 1 if embarked=="S" else 0

features = pd.DataFrame([{
    "Pclass": pclass,
    "Age": age,
    "Fare": fare,
    "SibSp": sibsp,
    "Parch": parch,
    "Sex_female": sex_female,
    "Sex_male": sex_male,
    "Embarked_C": embarked_C,
    "Embarked_Q": embarked_Q,
    "Embarked_S": embarked_S
}])

if st.button("Predict"):

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("Passenger Survived")
    else:
        st.error("Passenger Did Not Survive")