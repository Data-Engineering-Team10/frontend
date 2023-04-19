import streamlit as st
import psycopg2
import pandas as pd


st.set_page_config(
    page_title="Main page",
    page_icon="👋",
)


# Initialize connection.
# # Uses st.cache_resource to only run once.
# @st.cache_resource
# def init_connection():
#     return psycopg2.connect(**st.secrets["postgres"])

# conn = init_connection()

# # Perform query.
# # Uses st.cache_data to only rerun when the query changes or after 10 min.
# @st.cache_data(ttl=600)
# def run_query(query):
#     with conn.cursor() as cur:
#         cur.execute(query)
#         return cur.fetchall()

# rows = run_query("SELECT * from users;")

# # Print results.
# for row in rows:
#     st.write(f"user_id: {row[0]}, user_name: {row[1]}, password: {row[2]}, embeddings: {row[3]}:")
    
# # data = pd.DataFrame(rows, columns=['name', 'pet'])
# # st.table(data)
    

