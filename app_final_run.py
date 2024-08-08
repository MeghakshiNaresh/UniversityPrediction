import streamlit as st
import pandas as pd
import numpy as np
import pickle

clf = pickle.load(open("case_study_university_v1.pkl","rb"))

def predict(data):
     clf = pickle.load(open("case_study_university_v1.pkl","rb"))
     return clf.predict(data)

st.title("Case Study On University Admission Prediction")
st.markdown("Lets Predict Admission chances")

st.header("Chances for getting Admissiom")
col1,col2 = st.columns(2)

with col1:
    G= st.slider("GRE Score", 1.0, 350.0, 0.5)
    T= st.slider("TOEFL Score", 1.0, 120.0, 0.5)
    U= st.slider("University Rating", 1.0, 5, 1.0)
    S= st.slider("SOP", 1.0, 5.0, 1.0)
    L= st.slider("LOR", 1.0, 5.0, 1.0)
    C= st.slider("CGPA", 1.0, 10.0, 0.5)
    R= st.slider("Research", 1.0, 5.0, 0.5)
                          
st.text('')
if st.button("Predict Total Sales Price on Media "):
    result = predict(
        np.array([[G,T,U,S,L,C,R]]))
    st.text(result[0])    
st.markdown("Developed  at mala and meghakshi")


