import streamlit as st
from db import select_table, update_table, insert_table, get_embedding_vector
from streamlit_extras.let_it_rain import rain


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
        signup_button = st.button("Sign Up", key='login page')

    # Check if the username and password are correct
    if login_button:
        # If correct, change it to main page. Otherwise, warning pops up.
        try:
            query_result = select_table("users", where_dict={'user_name': username, 'password': password})
            st.write("<h1 style='text-align:center'>Welcome, {}!</h1>".format(username), unsafe_allow_html=True)
            st.write("<p style='text-align:center'>You have successfully logged in.</p>", unsafe_allow_html=True)
            st.write("<p style='text-align:center'>Enjoy your wine!</p>", unsafe_allow_html=True)
            
            st.session_state['login_flag'] = 'login'
            st.session_state['profile'] = query_result
        except Exception as e:
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
        signup_button = st.button("Sign Up", key='signup page')
    with col2:
        back_button = st.button("Back")

    # Check if the password and confirm password match
    if signup_button:
        try:
            row_dict = {'user_name': name,
                        'password': password,
                        'embeddings': get_embedding_vector()}
            query_result = insert_table("users", row_dict)

            rain(emoji="✨", font_size=54, falling_speed=2, animation_length="infinite")
            st.write("<h1 style='text-align:center'>Welcome, {}!</h1>".format(name), unsafe_allow_html=True)
            st.write("<p style='text-align:center'>You have successfully signed up.</p>", unsafe_allow_html=True)

            st.session_state['login_flag'] = 'login'
            st.session_state['profile'] = query_result
        except Exception as e:
            # TODO: 유저 테이블 구현하고 예외처리 다양화
            st.warning(e)

    if back_button:
        st.session_state['login_flag'] = 'logout'


# TODO: 메인페이지 구현
def main_page():
    st.markdown('# main page')


st.session_state.setdefault('login_flag', 'logout')
if st.session_state['login_flag'] == 'logout':
    login_page()
elif st.session_state['login_flag'] == 'signup':
    signup_page()
elif st.session_state['login_flag'] == 'login':
    main_page()

