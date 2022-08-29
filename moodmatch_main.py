import streamlit as st

st.title("Whats your Mood . . ?")

st.selectbox('Choose', ['Happy', 'Sad'])

input =  st.selectbox()
st.text(input)
