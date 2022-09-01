import streamlit as st
import time
import pandas as pd

st.title("How are You feeling Today?")

moods = ['Happy','Sad','Disgust','Afraid','Angry','Grateful','Nostalgic','Empathic','Romantic','Inspired','Broken','I dont know']
selected_mood = st.selectbox('Choose', moods)


st.header('Would you rather like a song or a quote?')
selected_choice = st.selectbox('Pick', ['Song','Quote'])

quotes=pd.read_csv('quotesDB.csv')

st.text (quotes['Rating'][0][3])
  
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

if(dict1[selected_mood]<11):
  max=0
  arr=[0]*6
  for i in range(0,5):
    # for j in np.arange(0,22,2):
    if(quotes["Rating"][i][dict1[selected_mood]] > max): 
        max=quotes["Rating"][i][dict1[selected_mood]
        arr[k]=i
        k+=1
    if(len(arr)==1): quote= quotes["List"][arr[0]]
    else: 
        rng = np.random.default_rng() # doing this is recommended by numpy
        non_zero = arr[arr!=0]
        rand=rng.choice(non_zero, 1, replace=False)
        quote= quotes["List"][arr[rand]]
        
if(selected_choice=='Quote'):
  with st.spinner(text='Loading the perfect Quote for you . . .'):
   time.sleep(4)
st.subheader(quote)
