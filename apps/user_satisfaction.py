import streamlit as st
import pandas as pd

def app():
    st.title('This is the User Satisfaction page')

    st.markdown('**This is the `User Satisfaction` of this the user analysis multi page.**')

    st.markdown('**In this app, we will see the data and some visualization of user engagement.**')
    
    st.title('User Experience data experience score')
    df = pd.read_csv('./data/user_exp_score.csv')
    st.write(df)
    st.title('User Engagment data with engagement score')
    df2 = pd.read_csv('./data/user_eng_score.csv')
    st.write(df2)
    st.title('Top clusters based on Experience score')
    st.image('https://i.ibb.co/jwmRWfp/exp-scr.png')
    st.title('Top clusters based on Engagement score')
    st.image('https://i.ibb.co/DWtH83B/eng-scr.png')