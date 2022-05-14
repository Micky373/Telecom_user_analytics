import streamlit as st
import pandas as pd

def app():
    st.title('This is the User Overview page')

    st.markdown('**This is the `User Overview` of this the user analysis multi page.**')

    st.markdown('**In this app, we will see the data and some visualization of user engagement.**')

    df = pd.read_csv('./data/user_overview_data.csv')
    st.write(df)
    st.title('Top 10 handsets used by the customers')
    st.image('https://i.ibb.co/hy63DgH/handsets.png')
    st.title('Top 3 manufacturers that provide handset to the users')
    st.image('https://i.ibb.co/tYqNhYP/manuf.png')
    st.title('Top 10 handset made by Apple company')
    st.image('https://i.ibb.co/BqvS2k9/apple-hand.png')
    st.title('Top 10 handset made by Huawei company')
    st.image('https://i.ibb.co/D1VbZGb/huawei-handset.png')
    st.title('Top 10 handset made by Samsung company')
    st.image('https://i.ibb.co/6g1rpCS/samsung-hand.png')
