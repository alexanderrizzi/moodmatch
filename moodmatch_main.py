import streamlit as st
import time

st.title("Whats your Mood . . ?")

emotions = ['Happy', 'Sad']
selected_emotion = st.selectbox('Choose', emotions)


st.header('Would you rather like a song or a quote?')
selected_choice = st.selectbox('Pick', ['Song','Quote'])

if(selected_choice=='Quote'):
  with st.spinner(text='Loading the perfect Quote for you . . .'):
   time.sleep(5)
  quote =  ' "The best revenge is not to be like that" - Marcus Aurelius '
  st.subheader(quote)
