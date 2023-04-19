import streamlit as st
from db import select_table, update_table, decode_vector
from streamlit_extras.let_it_rain import rain
import time


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

def login_page():
    # Create a login form
    st.write("<h1 style='text-align:center'>Login</h1>", unsafe_allow_html=True)
    username = st.text_input("Username", placeholder="New Jeans")
    password = st.text_input("Password", type="password")

    # Buttons
    col1, col2 = st.columns([1, 8])
    with col1:
        login_button = st.button("Login")
    with col2:
        signup_button = st.button("Sign Up")

    # Check if the username and password are correct
    if login_button:
        results, columns = select_table(
            "users", where_dict={'user_name': username, 'password': password}
        )

        # If correct, change it to main page. Otherwise, warning pops up.
        if results:
            st.write("<h1 style='text-align:center'>Welcome, {}!</h1>".format(username), unsafe_allow_html=True)
            st.write("<p style='text-align:center'>You have successfully logged in.</p>", unsafe_allow_html=True)
            st.write("<p style='text-align:center'>Enjoy your wine!</p>", unsafe_allow_html=True)
            st.session_state['login_flag'] = 'login'
        else:
            st.warning("Incorrect username or password")

    if signup_button:
        st.session_state['login_flag'] = 'signup'


def signup_page():
    # Create a sign up form
    st.write("<h1 style='text-align:center'>Sign Up</h1>", unsafe_allow_html=True)
    name = st.text_input("Name", placeholder="New Jeans")
    email = st.text_input("Email", placeholder="newjeanszzang@gm.gist.ac.kr")
    number = st.text_input("Phone Number", placeholder="010-1234-1234")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if password != confirm_password:
        st.warning("Passwords do not match. Please enter matching passwords.")
    address = st.selectbox("Address", ("쌍암동", "오룡동"))

    # Wine type
    st.subheader("What is your favorite wine type?")
    red = st.checkbox('Red wine')
    white = st.checkbox('White wine')

    # Light & Bold
    st.subheader("What kind of taste do you prefer?")
    lb_options = {'Lightest': 1, 'Light': 2, 'Medium': 3, 'Bold': 4, 'Boldest': 5}
    lb_flavor = st.select_slider('Light or Bold',
                              options=lb_options.keys(),
                              value='Medium')

    # Smooth & Tannic
    st_options = {'Smoothest': 1, 'Smooth': 2, 'Medium': 3, 'Tannic': 4, 'Most Tannic': 5}
    st_flavor = st.select_slider('Smooth or Tannic',
                               options=st_options.keys(),
                               value='Medium')

    # Dry & Sweet
    ds_options = {'Driest': 1, 'Dry': 2, 'Medium': 3, 'Sweet': 4, 'Sweetest': 5}
    ds_flavor = st.select_slider('Dry or Sweet',
                               options=ds_options.keys(),
                               value='Medium')

    # Soft & Acidic
    sa_options = {'Softest': 1, 'Soft': 2, 'Medium': 3, 'Acidic': 4, 'Most Acidic': 5}
    sa_flavor = st.select_slider('Soft or Acidic',
                               options=sa_options.keys(),
                               value='Medium')

    # Buttons
    col1, col2 = st.columns([9, 1])
    with col1:
        signup_button = st.button("Sign Up")
    with col2:
        logout_button = st.button("Back")

    # TODO: Sign up 만들기, Insert 만들기
    if signup_button:
        # Check if the password and confirm password match
        if password:
            # rain(
            #     emoji="✨",
            #     font_size=54,
            #     falling_speed=2,
            #     animation_length="infinite",
            # )
            # st.balloons()
            st.write("<h1 style='text-align:center'>Welcome, {}!</h1>".format(name), unsafe_allow_html=True)
            st.write("<p style='text-align:center'>You have successfully signed up.</p>", unsafe_allow_html=True)
            time.sleep(6)
            st.session_state['login_flag'] = 'login'

    if logout_button:
        st.session_state['login_flag'] = 'logout'

st.session_state.setdefault('login_flag', 'logout')
if st.session_state['login_flag'] == 'logout':
    login_page()
elif st.session_state['login_flag'] == 'signup':
    signup_page()
