import streamlit as st
import time
import pandas as pd

st.title("How are You feeling Today?")

moods = ['Happy','Sad','Disgust','Afraid','Angry','Grateful','Nostalgic','Empathic','Romantic','Inspired','Broken','I dont know']
selected_emotion = st.selectbox('Choose', moods)


st.header('Would you rather like a song or a quote?')
selected_mood = st.selectbox('Pick', ['Song','Quote'])

if(selected_choice=='Quote'):
  with st.spinner(text='Loading the perfect Quote for you . . .'):
   time.sleep(4)

quotes=pd.read_csv('quotesDB.csv')

for i in range(0,11):
  st.text (quotes['Rating'][1][i])

  dict1 = {
  "Happy": 0,
  "Sad": 1,
  "Disgust": 2 ,
  "Afraid": 3,
  "Angry": 4,
  "Grateful": 5, 
  "Nostalgic": 6,
  "Empathic": 7,
  "Romantic": 8,
  "Inspired": 9,
  "Broken": 10,
  "I dont know": 11
}
  
if (thisdict(selected_mood)<12):
  st.text("ss")
