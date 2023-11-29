import streamlit as st
import pickle

# load the pickled model
with open('model_lr.pkl','rb') as file:
    model_lr=pickle.load(file)

# create streamlit web app for linear regression to predict salary
st.header('Welcome to the Salary Predictor App')

st.write('Salary Predictor App. This app predicts your salary on the basis of your marks')

st.sidebar.header('Please select your marks')

marks = st.sidebar.slider('Input Marks to get salary',0,100,1)

st.write('Marks are: ',marks)

yhat = model_lr.predict([[marks]])

st.write('yhat is ',yhat)