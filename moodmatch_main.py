import streamlit as st

st.title("Whats your Mood . . ?")


emotions = ['Happy', 'Sad']
selected_emotion = st.selectbox('Choose', emotions)


st.header('Would you rather like a song or a quote?')
selected_choice = st.selectbox('Pick', ['Song','Quote'])
