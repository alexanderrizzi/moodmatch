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
    rating_arr=np.zeros(6)
    pos_arr=np.zeros(6)
    del_arr=[]
    for i in range(0,6):
      if(int(quotes["Rating"][i][dict1[selected_mood]])>=max):
            max=int(quotes["Rating"][i][dict1[selected_mood]])
            rating_arr[i]=int(quotes["Rating"][i][dict1[selected_mood]])
            pos_arr[i]=i
    #st.text(max) 
    for i in range(0,len(rating_arr)):
      if(rating_arr[i]!=max) : 
        del_arr.append(i)
    pos_arr=np.delete(pos_arr,del_arr)
    #rating_arr=rating_arr[rating_arr==max]
    #st.text(pos_arr)
    
    rnd=random.choice(pos_arr)
    quote= quotes["List"][rnd]
    author=quotes["Author"][rnd]
    
if(selected_choice=='Quote'):
  with st.spinner(text='Loading the perfect Quote for you . . .'):
   time.sleep(2)
  st.header('"'+quote+'"')
  st.subheader('-- ' + author)
  
time.sleep(2)

st.header('How well did the quote match your mood?')
feedback=st.slider('Pick', 0, 5)

if(feedback>2):
  updated_rating=int(quotes["Rating"][i][dict1[selected_mood]]) + feedback/5
  quotes.loc[rnd, 'Rating'] = updated_rating
  quotes.to_csv("AllDetails.csv", index=True)
 
else:
  updated_rating=int(quotes["Rating"][i][dict1[selected_mood]]) - feedback/5
  quotes.loc[rnd, 'Rating'] = updated_rating
  quotes.to_csv("AllDetails.csv", index=True)
st.dataframe(quotes)
