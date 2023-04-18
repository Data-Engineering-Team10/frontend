import streamlit as st
import base64
import numpy as np
import pandas as pd
from sqlalchemy import create_engine


st.set_page_config(
    layout="wide",  # Can be "centered" or "wide".
    initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
    page_title="Main page",
    page_icon="👋",
)


# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    config = st.secrets["postgres"]
    host = config["host"]
    port = config["port"]
    dbname = config["dbname"]
    user = config["user"]
    password = config["password"]
    return create_engine(f"postgresql://{user}:{password}@{host}:{port}/{dbname}")


# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query, _conn):
    return pd.read_sql_query(query, _conn)


# Decode serialized vector into real number array
@st.cache_data
def decode_vector(string_vec):
    # base85 문자열을 byte 타입으로 디코딩
    v_decode = base64.b85decode(string_vec)

    # random_v 와 동일한 vector로 복원
    original_v = np.frombuffer(v_decode, dtype=np.float32)
    return original_v


conn = init_connection()


# User Data
st.markdown("# User Data")

# query asks
resps = run_query("SELECT user_name, password, embeddings from users;", conn)
resps["embeddings"] = resps["embeddings"].apply(decode_vector)

# Print results.
st.dataframe(resps[:10])


# Wine Data
st.markdown("# Wine Data")

# query asks
resps = run_query(
    "SELECT wine_name, wine_type, continent, country, embeddings from wines;", conn
)
resps["wine_type"] = resps["wine_type"].apply(lambda x: "White" if x else "Red")
resps["embeddings"] = resps["embeddings"].apply(decode_vector)

# Print results.
st.dataframe(resps[:10])
