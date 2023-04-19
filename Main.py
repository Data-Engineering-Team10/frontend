import streamlit as st
import base64
import numpy as np
import pandas as pd
import psycopg2


st.set_page_config(
    layout="wide",  # Can be "centered" or "wide".
    initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
    page_title="Main page",
    page_icon="👋",
)


@st.cache_resource
def init_connection():
    """ Initialize connection. Uses st.cache_resource to only run once

    Returns:
        Connect: database connection
    """
    return psycopg2.connect(**st.secrets["postgres"])


def select_table(table_name, column_list=None, where_dict=None, order_by=None):
    """ Perform query, return it into pd.DataFrame

    Args:
        table_name (str): database table name
        column_list (list, optional): columns for query. Defaults to None.
        where_dict (dict, optional): {column name: value} Defaults to None.
        order_by (str, optional): ordering strategy. Defaults to None.

    Returns:
        pd.DataFrame: query result.
    """

    @st.cache_data
    def convert(results, columns):
        """ Transform query into pd.DataFrame

        Args:
            results (query): database query
            columns (list): column list

        Returns:
            pd.DataFrame: _description_
        """
        return pd.DataFrame(results, columns=columns)

    if column_list is None:
        column_clause = "*"
    else:
        column_clause = ", ".join(column_list)

    query = f"SELECT {column_clause} FROM {table_name}"
    values = []

    if where_dict is not None:
        where_clause = " AND ".join([f"{k} = %s" for k in where_dict.keys()])
        query += f" WHERE {where_clause}"
        values = list(where_dict.values())

    if order_by is not None:
        query += f" ORDER BY {order_by}"

    with conn.cursor() as cur:
        cur.execute(query, values)
        results = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        results = convert(results, columns)
        return results


def update_table(table_name, update_dict, where_dict):
    """ Update database table

    Args:
        table_name (str): database table name
        update_dict (dict): {column name: value}
        where_dict (dict): {column name: value}
    """
    update_clause = ", ".join([f"{k} = %s" for k in update_dict.keys()])
    where_clause = " AND ".join([f"{k} = %s" for k in where_dict.keys()])
    query = f"UPDATE {table_name} SET {update_clause} WHERE {where_clause}"
    values = list(update_dict.values()) + list(where_dict.values())
    with conn.cursor() as cur:
        cur.execute(query, values)


@st.cache_data
def decode_vector(string_vec):
    """ Decode serialized vector into real number vector

    Args:
        string_vec (str): serialized vector

    Returns:
        np.array: real number vector
    """
    # base85 문자열을 byte 타입으로 디코딩
    v_decode = base64.b85decode(string_vec)

    # random_v 와 동일한 vector로 복원
    original_v = np.frombuffer(v_decode, dtype=np.float32)
    return original_v


# Connect Database
conn = init_connection()

################ Displaying User data
st.markdown("# User Data")

# query asks
results = select_table(
    "users", column_list=None, where_dict=None, order_by="user_id ASC"
)
results["embeddings"] = results["embeddings"].apply(decode_vector)

# Print results.
st.dataframe(results)


################ Displaying Wine data
st.markdown("# Wine Data")

# query asks
column_list = ["wine_name", "wine_type", "continent", "country", "embeddings"]
results = select_table(
    "wines", column_list=column_list, where_dict=None, order_by="wine_id ASC",
)
results["wine_type"] = results["wine_type"].apply(lambda x: "White" if x else "Red")
results["embeddings"] = results["embeddings"].apply(decode_vector)

# Print results.
st.dataframe(results)


################ Updating User data
st.markdown("# Update user 1")

# query asks
update_dict = {"user_name": "바꼈지롱", "password": "unholy"}
where_dict = {"user_id": 1}
update_table("users", update_dict, where_dict)


where_dict = {"user_id": 1}
results = select_table(
    "users", column_list=None, where_dict=None, order_by="user_id ASC"
)
results["embeddings"] = results["embeddings"].apply(decode_vector)

# Print results.
st.dataframe(results)
