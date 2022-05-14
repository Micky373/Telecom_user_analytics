import streamlit as st
from multiapp import MultiApp
from apps import user_engagement, user_experience, user_overview, user_satisfaction # import your app modules here

app = MultiApp()

st.markdown("""
# Multi-Page App
This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
""")

# Add all your application here
app.add_app("User Overview", user_overview.app)
app.add_app("User Engagement", user_engagement.app)
app.add_app("User Experience", user_experience.app)
app.add_app("User Satisfaction", user_satisfaction.app)
# The main app
app.run()