import streamlit as st
from st_pages import Page, show_pages, add_page_title

st.title("Intro")
st.write("# YouTube Data Analyser")
st.markdown(
    """
    This app is built on account of an online course project.
    
    ### Problem statement:
    
    The problem statement is to create a Streamlit application that allows users to access and analyze data from multiple YouTube channels. The application should have the following features:
    - Ability to input a YouTube channel ID and retrieve all the relevant data (Channel name, subscribers, total video count, playlist ID, video ID, likes, dislikes, comments of each video) using Google API.
    - Ability to collect data for up to 10 different YouTube channels and store them in the data lake by clicking a button.
    - Option to store the data in a MYSQL or PostgreSQL.
    - Ability to search and retrieve data from the SQL database using different search options, including joining tables to get channel details.


    👈 Select a page!

    ### Demo

    - Walkthrough video - []()

    ### Developer

    - Personal Website - [nandhadesparrow.com](https://www.nandhadesparrow.com)
"""
)

