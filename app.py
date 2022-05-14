import streamlit as st
from multiapp import MultiApp
from apps import user_engagement, user_experience, user_overview, user_satisfaction # import your app modules here

app = MultiApp()

st.sidebar.markdown('# **Tellco Customers Analysis**')
st.sidebar.markdown("""
Before investing on a business it is a must to have best understanding about the field. This project is all about analyzing TellCo's user and find out whether it is worth buying or selling.
""")

# Add all your application here
app.add_app("User Overview", user_overview.app)
app.add_app("User Engagement", user_engagement.app)
app.add_app("User Experience", user_experience.app)
app.add_app("User Satisfaction", user_satisfaction.app)
# The main app
app.run()