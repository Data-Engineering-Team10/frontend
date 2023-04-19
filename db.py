import streamlit as st
import base64
import numpy as np
import pandas as pd
import psycopg2


@st.cache_resource
def init_connection():
    """ Initialize connection. Uses st.cache_resource to only run once

    Returns:
        Connect: database connection
    """
    return psycopg2.connect(**st.secrets["postgres"])


def select_table(table_name, column_list=None, where_dict=None, order_by=None):
    """ Perform query, return its query and columns

    Args:
        table_name (str): database table name
        column_list (list, optional): columns for query. Defaults to None.
        where_dict (dict, optional): {column name: value} Defaults to None.
        order_by (str, optional): ordering strategy. Defaults to None.

    Returns:
        results: query result.
        columns: columns of result.
    """

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

    with init_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, values)
            results = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            return results, columns


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

    with init_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, values)


@st.cache_data
def convert(results, columns):
    """ Transform query into pd.DataFrame

    Args:
        results (query): database query
        columns (list): column list

    Returns:
        pd.DataFrame: query data frame
    """
    return pd.DataFrame(results, columns=columns)


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
