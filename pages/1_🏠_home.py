import streamlit as st
import pandas as pd
import folium
from PIL import Image
import requests


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)


@st.cache_data
def fetch_wine(url):
    image = Image.open(requests.get(url, stream=True).raw)
    return image


tcol1, tcol2 = st.columns(2)
with tcol1:
    image = fetch_wine("https://cdn.pixabay.com/photo/2016/07/26/16/16/wine-1543170_960_720.jpg")
    st.image(image, caption="")
with tcol2:
    st.title("Welcome, we are WinePickers")



st.subheader("000, your current location is 0000")  #### user id, user 주소

st.write(" ")

st.subheader("Top 5 wines of this week")

# 예시 이미지
image_1 = "https://via.placeholder.com/300"
image_2 = "https://via.placeholder.com/300"

# 예시 이미지별 정보
info_1 = "이미지 1 정보"
info_2 = "이미지 2 정보"

# row 분할
col1, col2, col3, col4, col5 = st.columns(5)

# 각 column에 이미지와 정보 배치
with col1:
    st.image(image_1)  # 와인 사진
    st.write(info_1)  # 이름

with col2:
    st.image(image_2)
    st.write(info_2)

with col3:
    st.image(image_2)
    st.write(info_2)

with col4:
    st.image(image_2)
    st.write(info_2)

with col5:
    st.image(image_2)
    st.write(info_2)

st.markdown(" ")
st.markdown(" ")

#############3
st.subheader("These wines are also likely to be popular!")
# 예시 이미지
image_1 = "https://via.placeholder.com/300"
image_2 = "https://via.placeholder.com/300"

# 예시 이미지별 정보
info_1 = "이미지 1 정보"
info_2 = "이미지 2 정보"

# row 분할
col1, col2, col3, col4, col5 = st.columns(5)

# 각 column에 이미지와 정보 배치
with col1:
    st.image(image_1)  # 와인 사진
    st.write(info_1)  # 이름

with col2:
    st.image(image_2)
    st.write(info_2)

with col3:
    st.image(image_2)
    st.write(info_2)

with col4:
    st.image(image_2)
    st.write(info_2)

with col5:
    st.image(image_2)
    st.write(info_2)
st.markdown(" ")
st.markdown(" ")
############3

st.subheader("000's wine purchase list")
# 예시 이미지
image_1 = "https://via.placeholder.com/300"
image_2 = "https://via.placeholder.com/300"

# 예시 이미지별 정보
info_1 = "이미지 1 정보"
info_2 = "이미지 2 정보"

# row 분할
col1, col2, col3, col4, col5 = st.columns(5)

# 각 column에 이미지와 정보 배치
with col1:
    st.image(image_1)  # 와인 사진
    st.write(info_1)  # 이름

with col2:
    st.image(image_2)
    st.write(info_2)

with col3:
    st.image(image_2)
    st.write(info_2)

with col4:
    st.image(image_2)
    st.write(info_2)

with col5:
    st.image(image_2)
    st.write(info_2)
st.markdown(" ")
st.markdown(" ")

################

st.subheader("You might love these wines too!")
# 예시 이미지
image_1 = "https://via.placeholder.com/300"
image_2 = "https://via.placeholder.com/300"

# 예시 이미지별 정보
info_1 = "이미지 1 정보"
info_2 = "이미지 2 정보"

# row 분할
col1, col2, col3, col4, col5 = st.columns(5)

# 각 column에 이미지와 정보 배치
with col1:
    st.image(image_1)  # 와인 사진
    st.write(info_1)  # 이름

with col2:
    st.image(image_2)
    st.write(info_2)

with col3:
    st.image(image_2)
    st.write(info_2)

with col4:
    st.image(image_2)
    st.write(info_2)

with col5:
    st.image(image_2)
    st.write(info_2)

