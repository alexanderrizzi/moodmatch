import streamlit as st
import time
import pandas as pd

st.title("How are You feeling Today?")

moods = ['Happy','Sad','Disgust','Afraid','Angry','Grateful','Nostalgic','Empathic','Romantic','Inspired','Broken','I dont know']
selected_emotion = st.selectbox('Choose', moods)


st.header('Would you rather like a song or a quote?')
selected_choice = st.selectbox('Pick', ['Song','Quote'])

if(selected_choice=='Quote'):
  with st.spinner(text='Loading the perfect Quote for you . . .'):
   time.sleep(4)

quotes=pd.read_csv('quotesDB.csv')

st.text (quotes['Rating'][2][1])

