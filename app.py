import streamlit as st

st.title ("IITM BSC Data Science - Multiplication APP")
st.subheader (" Welcome to Multiplication of 2 given numbers APP - You can Multiply Two Numbers")

a = st.number_input('Enter the First number')
b = st.number_input('Enter the Second number')
result = a * b
st.write(a, ' * ', b , '= ', result)

