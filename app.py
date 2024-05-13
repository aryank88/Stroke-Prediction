import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('modelx.pkl', 'rb'))

st.header('Predict Stroke :brain:')
st.text('Yes: 1 and No: 0')
st.text('Residence type - Urban: 1 and Rural: 0')

age = st.slider("Age", 1, 85)
ever_married = st.selectbox("Married", ["0", "1"])
bmi = st.slider("BMI", 10.0, 50.0)
Residence_type = st.selectbox("Residence", ["1", "0"])
Never_worked = st.radio("Working?", ["1", "0"])
hypertension = st.selectbox("hypertension", ["1", "0"])
Govt_job = st.radio("Govt_job?", ["1", "0"])
heart_disease = st.radio("Heart Disease?", ["1", "0"])

def predict():
    float_features = [float(x) for x in [bmi]]
    categorical_features = [ever_married,Residence_type,Never_worked,hypertension,Govt_job,heart_disease]
    integer_features = [age]

    final_features = [np.array(float_features + integer_features + categorical_features)]
    prediction = model.predict(final_features)
    label = prediction[0]
   
    print(type(label))
    print(label)

    st.success('The Prediction is : ' + str(label))
   
trigger = st.button('Predict', on_click=predict)
