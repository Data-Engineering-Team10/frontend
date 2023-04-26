import streamlit as st
import pandas as pd
import folium
from PIL import Image
import requests
import random
import math

wine_info = pd.read_csv('./.streamlit/vivino_dataset.csv')

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

@st.cache_data
def fetch_wine(url):
    image = Image.open(requests.get(url, stream=True).raw)
    return image

# top 
tcol1, tcol2 = st.columns(2)
with tcol1:
    image = fetch_wine("https://cdn.pixabay.com/photo/2016/07/26/16/16/wine-1543170_960_720.jpg")
    st.image(image, caption="")
with tcol2:
    st.title("Welcome, we are WinePickers ✨")


st.subheader("000, your current location is 0000")  #### user id, user 주소
# st.subheader("{}, your current location is {}".format(name, location))  #### user id, user 주소

st.write(" ")

st.subheader("Top 5 wines of this week")

def get_random_image_url_info():
    select = random.randrange(0, 500)
    image_url = wine_info['imgurl'][select]
    image_info = wine_info['name'][select]
    return image_url, image_info

def popualr_image_url_info():
    select = random.randrange(500, 700)
    image_url = wine_info['imgurl'][select]
    image_info = wine_info['name'][select]
    return image_url, image_info

# 예시 이미지
image_1, info_1 = get_random_image_url_info()
image_2, info_2 = get_random_image_url_info()
image_3, info_3 = get_random_image_url_info()
image_4, info_4 = get_random_image_url_info()
image_5, info_5 = get_random_image_url_info()

# row 분할
col1, col2, col3, col4, col5 = st.columns(5)

# 각 column에 이미지와 정보 배치
with col1:
    st.image(image_1,width=50)  # 와인 사진
    st.write(info_1)  # 이름

with col2:
    st.image(image_2,width=50)
    st.write(info_2)

with col3:
    st.image(image_3,width=50)
    st.write(info_3)

with col4:
    st.image(image_4,width=50)
    st.write(info_4)

with col5:
    st.image(image_5,width=50)
    st.write(info_5)

st.markdown(" ")
st.markdown(" ")

#############3
st.subheader("These wines are also likely to be popular!")

image_1, info_1 = popualr_image_url_info()
image_2, info_2 = popualr_image_url_info()
image_3, info_3 = popualr_image_url_info()
image_4, info_4 = popualr_image_url_info()
image_5, info_5 = popualr_image_url_info()
# row 분할
col1, col2, col3, col4, col5 = st.columns(5)

# 각 column에 이미지와 정보 배치
with col1:
    st.image(image_1,width=50)  # 와인 사진
    st.write(info_1)  # 이름

with col2:
    st.image(image_2,width=50)
    st.write(info_2)

with col3:
    st.image(image_3,width=50)
    st.write(info_3)

with col4:
    st.image(image_4,width=50)
    st.write(info_4)

with col5:
    st.image(image_5,width=50)
    st.write(info_5)
st.markdown(" ")
st.markdown(" ")
############



# TODO : get embedding info 

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

