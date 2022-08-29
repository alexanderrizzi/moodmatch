import streamlit as st

st.title("Whats your Mood . . ?")


emotions = ['Happy', 'Sad']
selected_emotion = st.selectbox('Choose', emotions)

input =  selected_emotion
st.text(input)
