import streamlit as st
import pandas as pd

def app():
    st.title('This is the User Experience page')

    st.markdown('**This is the `User Experience` of this the user analysis multi page.**')

    st.markdown('**In this app, we will see the data and some visualization of user engagement.**')

    df = pd.read_csv('./data/user_experience.csv')
    st.write(df)
    st.title('Top 10 customers based on TP')
    st.image('https://i.ibb.co/NC1dzWy/TP-top.png')
    st.title('Top 10 customers based on RTT')
    st.image('https://i.ibb.co/cxNnSqd/RTT-top.png')
    st.title('Top 10 customers based on TCP')
    st.image('https://i.ibb.co/2M9yFVc/TCP-top.png')
    

