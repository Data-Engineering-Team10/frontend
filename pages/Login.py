import streamlit as st
#import psycopg2
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)



# def signup():
#     st.title('와인 3')
#     st.write(st.session_state.get('message', ''))
#     if st.button('뒤로가기'):
#         st.session_state['main_page'] = 'main_page'



def main_login():
    with st.container():
        # Create a login form
        st.write("<h1 style='text-align:center'>Login</h1>", unsafe_allow_html=True)
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
        with col1:
            login_button = st.button("Login")
        with col2:
            signup_button = st.button("Sign Up")


        if login_button:
            # Check if the username and password are correct
            if username == "user" and password == "password":
                # Hide the login form and show a welcome message
                st.write("<h1 style='text-align:center'>Welcome, {}!</h1>".format(username), unsafe_allow_html=True)
                st.write("<p style='text-align:center'>You have successfully logged in.</p>", unsafe_allow_html=True)
                st.write("<p style='text-align:center'>Enjoy your wine!</p>", unsafe_allow_html=True)

            else:
                st.warning("Incorrect username or password")
        if signup_button:
            st.session_state['main_login'] == 'signup'
            switch_page("Sign Up")



st.session_state.setdefault('main_login', 'main_login')
if st.session_state['main_login'] == 'main_login':
    main_login()
# elif st.session_state['main_login'] == 'signup':
#     # signup()

