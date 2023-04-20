import streamlit as st
import psycopg2
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.let_it_rain import rain
import time

with st.container():
    # Create a sign up form
    st.write("<h1 style='text-align:center'>Sign Up</h1>", unsafe_allow_html=True)
    st.write('')
    st.write('')
    name = st.text_input("Name")
    st.write('')
    email = st.text_input("Email")
    st.write('')
    number = st.text_input("Phone Number")
    st.write('')

    password = st.text_input("Password", type="password")
    st.write('')

    confirm_password = st.text_input("Confirm Password", type="password")
    st.write('')

    address = st.text_input("Address")
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.subheader("What is your favorite wine type?")
    red = st.checkbox('Red wine')
    if red:
        st.write("That's good!")
        # 데이터에 값 넘겨주기
    
    white = st.checkbox('White wine')
    if white:
        st.write("That's good!")
        # 데이터에 값 넘겨주기

    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.subheader("What kind of taste do you prefer?")
    values = ['Light', 10,20,30,40,50,60,70,80,90,'Bold']    
    flavor = st.select_slider('', options = values, key='flavor')
    if flavor == 'Light': flavor = 0
    if flavor == 'Bold': flavor = 100

    values2 = ['Smooth', 10,20,30,40,50,60,70,80,90,'Tannic']    
    flavor2 = st.select_slider('', options = values2, key='flavor2')
    if flavor2 == 'Smooth': flavor2 = 0
    if flavor2 == 'Tannic': flavor2 = 100

    values3 = ['Dry', 10,20,30,40,50,60,70,80,90,'Sweet']
    flavor3 = st.select_slider('', options = values3, key='flavor3')
    if flavor3 == 'Dry': flavor3 = 0
    if flavor3 == 'Sweet': flavor3 = 100

    values4 = ['Soft', 10,20,30,40,50,60,70,80,90,'Acidic']
    flavor4 = st.select_slider('', options = values4, key='flavor4')
    if flavor4 == 'Soft': flavor4 = 0
    if flavor4 == 'Acidic': flavor4 = 100


    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')


    sign_up_button = st.button("Done!")   # 로그인 페이지로 이동.
    
    if sign_up_button:
        # Check if the password and confirm password match
        if password == confirm_password:
            # TODO: Perform sign up logic and show a success message
            rain(
                emoji="✨",
                font_size=54,
               falling_speed=2,
                animation_length="infinite",
            )
            # st.balloons()
            st.write('')
            st.write('')
            st.header('')
            st.write("<h1 style='text-align:center'>Welcome, {}!</h1>".format(name), unsafe_allow_html=True)
            st.write("<p style='text-align:center'>You have successfully signed up.</p>", unsafe_allow_html=True)
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            time.sleep(6)
            switch_page("Login")
        else:
            st.warning("Password and confirm password do not match")