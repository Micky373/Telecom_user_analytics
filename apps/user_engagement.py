import streamlit as st
import pandas as pd

def app():
    st.title('This is the User Engagement page')

    st.markdown('**This is the `User Engagement` of this the user analysis multi page.**')

    st.markdown('**In this app, we will see the data and some visualization of user engagement.**')

    df = pd.read_csv('./data/user_engegement_data.csv')
    st.write(df)
    st.image('https://i.ibb.co/K5J22Sm/Netflix.png')
    st.image('https://i.ibb.co/YfDsTdX/Youtube.png')
    st.image('https://i.ibb.co/0KBBcwr/Google.png')
    st.image('https://i.ibb.co/TrhJZsg/Gaming.png')