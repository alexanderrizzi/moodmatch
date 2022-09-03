import streamlit as st
import time
import pandas as pd
import numpy as np
import math
import random

st.title("How are You feeling Today?")

moods = ['Happy','Sad','Disgust','Afraid','Angry','Grateful','Nostalgic','Empathic','Romantic','Inspired','Broken','I dont know']
selected_mood = st.selectbox('Choose', moods)


st.header('Would you rather like a song or a quote?')
selected_choice = st.selectbox('Pick', ['Song','Quote'])

quotes=pd.read_csv('quotesDB.csv')
  
dict1 = {
  "Happy": 0,
  "Sad": 2,
  "Disgust": 4 ,
  "Afraid": 6,
  "Angry": 8,
  "Grateful": 10, 
  "Nostalgic": 12,
  "Empathic": 14,
  "Romantic": 16,
  "Inspired": 18,
  "Broken": 20,
  "I dont know": 22
}


if(dict1[selected_mood]<22):
    max=-math.inf
    arr=np.zeros(6)
    for i in range(0,6):
        if(int(quotes["Rating"][i][dict1[selected_mood]]) > max):
            st.text(quotes["Rating"][i][dict1[selected_mood]])
            max=int(quotes["Rating"][i][dict1[selected_mood]])
            arr[i]=i
    st.text(max) 
    arr=arr[arr==max]
    st.text(arr)
    if(len(arr)==1): quote= quotes["List"][arr[0]]    
    else: 
        rnd=random.randint(1,len(arr))
        quote= quotes["List"][rnd]
        
if(selected_choice=='Quote'):
  with st.spinner(text='Loading the perfect Quote for you . . .'):
   time.sleep(2)
  st.subheader(quote)

