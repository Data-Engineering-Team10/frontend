from db import *
from models import *

import streamlit as st
from streamlit_extras.let_it_rain import rain


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

def login_page():
    """ Login Page """
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
    """ Sign up Page """
    # Create a sign up form
    st.write("<h1 style='text-align:center'>Sign Up</h1>", unsafe_allow_html=True)
    name = st.text_input("Name", placeholder="New Jeans")
    # email = st.text_input("Email", placeholder="newjeanszzang@gm.gist.ac.kr")
    # phone = st.text_input("Phone Number", placeholder="010-1234-1234")
    password = st.text_input("Password", type="password")
    address = st.selectbox("Address", ("쌍암동", "오룡동"))

    # Wine type
    st.subheader("What is your favorite wine type?")
    wine_type = st.radio("", ('Red wine', 'White wine'), label_visibility='collapsed')
    wine_type = wine_type.split()[0]

    # Wine taste
    st.subheader("What kind of taste do you prefer?")
    bold = float(st.select_slider('Light(0) ~ Bold(1)', options=[f'{0.1*i:.1f}' for i in range(11)], value='0.5'))
    tannic = float(st.select_slider('Smooth(0) ~ Tannic(1)', options=[f'{0.1*i:.1f}' for i in range(11)], value='0.5'))
    sweet = float(st.select_slider('Dry(0) ~ Sweet(1)', options=[f'{0.1*i:.1f}' for i in range(11)], value='0.5'))
    acidic = float(st.select_slider('Soft(0) ~ Acidic(1)', options=[f'{0.1*i:.1f}' for i in range(11)], value='0.5'))

    # Buttons
    col1, col2 = st.columns([9, 1])
    with col1:
        signup_button = st.button("Sign Up", key='signup page')
    with col2:
        back_button = st.button("Back")

    # Check if the password and confirm password match
    if signup_button:
        try:
            embeddings = get_initial_vec(model, df_wine, wine_type, bold, tannic, sweet, acidic)
            embeddings = encode_vector(embeddings)
            
            row_dict = {'user_name': name,
                        'password': password,
                        'address': address,
                        'wine_type': wine_type,
                        'bold': bold,
                        'tannic': tannic,
                        'sweet': sweet,
                        'acidic': acidic,
                        'embeddings': embeddings}
            
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
    """ Main Page """
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<center><img src=https://cdn.pixabay.com/photo/2016/07/26/16/16/wine-1543170_960_720.jpg style='display: block; width: 500px;'></center>", unsafe_allow_html=True)
    with col2:
        st.title("Welcome, we are WinePickers ✨")
        
    st.subheader(f"{st.session_state['profile']['user_name'][0]}, your current location is {st.session_state['profile']['address'][0]}")

    recommendation = recommend_wine(df_embedding, st.session_state['profile']['embeddings'][0])
    recommendation_df = df_wine.loc[recommendation.iloc[:200].index]

    st.subheader("Top 5 wines of this week")
    with st.container():
        columns = st.columns(5)
        for i in range(len(columns)):
            url = recommendation_df['url'].values[i]
            wine_name = recommendation_df['wine_name'].values[i]
            columns[i].markdown(f"<center><img src={url} style='display: block; width: 100px;'></center>", unsafe_allow_html=True)
            
    with st.container():
        columns = st.columns(5)
        for i in range(len(columns)):
            wine_name = recommendation_df['wine_name'].values[i]
            columns[i].markdown(f"<center>{wine_name}</center>", unsafe_allow_html=True)

    st.subheader("Top wine continents you may like.")
    with st.container():
        recommend_continent = best_continent(recommendation_df, model.encoder.embedding)
        columns = st.columns(min(len(recommend_continent), 5))
        for i in range(len(columns)):
            columns[i].markdown(f"{i+1}. {recommend_continent[i]}")
    
    st.subheader("Top grape breeds you may like.")
    with st.container():
        recommend_grapes = best_grapes(recommendation_df, model.encoder.embedding)
        columns = st.columns(min(len(recommend_grapes), 5))
        for i in range(len(columns)):
            columns[i].markdown(f"{i+1}. {recommend_grapes[i]}")
            
    st.subheader("Top countries you may like.")
    with st.container():
        recommend_counties = best_countries(recommendation_df, model.encoder.embedding)
        columns = st.columns(min(len(recommend_counties), 5))
        for i in range(len(columns)):
            columns[i].markdown(f"{i+1}. {recommend_counties[i]}")
    
    
    # Wine recommendation
    st.subheader("How about the recommended wine?")
    wine = st.selectbox('', (df_wine['wine_name']), label_visibility='collapsed')
    wine_idx = df_wine[df_wine['wine_name'] == wine].index

    rate = float(st.select_slider('Please select update rate. Higher value will update more.', options=[f'{0.5*i:.1f}' for i in range(11)], value='2.5'))

    target_wine_vec = df_embedding[wine_idx]
    update = st.button('update')

    if update:
        updated_embeddings = update_my_vec(st.session_state['profile']['embeddings'][0], target_wine_vec, rate)
        embeddings = encode_vector(updated_embeddings[0])
        update_log = update_table('users', {'embeddings': embeddings}, {'user_name': st.session_state['profile']['user_name'][0]})
        st.markdown(update_log)
        
        # import time
        # time.sleep(5)
        # st.experimental_rerun()


model = load_model()
df_wine = select_table('wines')
df_embedding = df_wine[['embeddings']].iloc[:, 0].values
df_embedding = np.stack(df_embedding)

st.session_state.setdefault('login_flag', 'logout')
if st.session_state['login_flag'] == 'logout':
    login_page()
elif st.session_state['login_flag'] == 'signup':
    signup_page()
elif st.session_state['login_flag'] == 'login':
    main_page()

