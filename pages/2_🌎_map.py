import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium, folium_static
import random
import math
import numpy as np
from db import *


# st.set_page_config(
#     page_title="Hello",
#     layout='wide'
# )

# TODO : TOY MARKET DB 에서 가져오기, 지금은 임시로 대충 해놓음

wine_info = pd.read_csv('./.streamlit/vivino_dataset.csv')

# 10
max_price_range = [99.5, 99.8, 99.7, 99.6, 99.5, 99.4, 99.3, 99.1, 99]
min_price_range = [98.9, 98.7, 98.3, 98, 97.8, 96, 95, 94, 90]

select = random.randrange(0, 10)

df_wine = select_table('wines')

def main_page():

    col1, col2 = st.columns([4,3])

    with col1:
        st.title('Which wine are you looking for?🍷')
        wine = st.selectbox('', (df_wine['wine_name']), label_visibility='collapsed')
        wine_idx = df_wine[df_wine['wine_name'] == wine].index

        if st.button('Search'):
            if wine.strip():  # 코드 입력란에 공백이 아닌 문자가 입력되었을 경우
                with col2:
                    search_page(wine)
            else:
                st.error('Please enter a valid search term.')  # 코드 입력란에 공백이 입력되었을 경우 에러 메시지 출력



    st.title('지도 🎈')
    m = folium.Map(location=[35.228956, 126.843181], zoom_start=16)
    folium.Marker(
        [35.228956, 126.843181],
        popup='GIST',
        tooltip='Dasan'
    ).add_to(m)
    
    inventoryA=''
    for i in range(18) : # 18개
        inventoryA = inventoryA + wine_info['name'][i] + '\n - '

    markerA = folium.Marker(
        [35.22115148181801, 126.84508234413954],
        popup=folium.Popup(inventoryA[:-2], max_width=250),
        tooltip='MARKET A'
    ).add_to(m)

    inventoryB=''
    for i in range(18, 30) : # 12개
        inventoryB = inventoryB + wine_info['name'][i] + '\n - '

    markerB = folium.Marker(
        [35.22359306367261, 126.85141562924461],
        popup=folium.Popup(inventoryB[:-2], max_width=250),
        tooltip='MARKET B'
    ).add_to(m)

    inventoryC=''
    for i in range(30, 60) : #30개
        inventoryC = inventoryC + wine_info['name'][i] + '\n - '

    markerC = folium.Marker(
        [35.221234713907336, 126.8540341090701],
        popup=folium.Popup(inventoryC[:-2], max_width=300),
        tooltip='MARKET C'
    ).add_to(m)

    folium.Marker(
        location=[35.234738, 126.838680],
        icon=folium.Icon(color="red"),
        popup=folium.Popup("I'm a red marker", max_width=300),
        tooltip='Red Marker'
    ).add_to(m)

    st_data = st_folium(m, width=725)

    st.title('와인 매장을 보여드릴게요 🐾')

        
    if st.button('MARKET A'):
        st.session_state['main_page'] = 'page1'
        st.dataframe(wine_info[['name','cost']][0:18])
            
    if st.button('MARKET B'):
        st.session_state['main_page'] = 'page2'
        st.dataframe(wine_info[['name','cost']][18:30])
        
    if st.button('MARKET C'):
        st.session_state['main_page'] = 'page3'
        st.dataframe(wine_info[['name','cost']][30:60])

mins = 90.0
maxs = 101.2
def search_page(code):

    # 와인 재고 toy data
    inventoryA = wine_info.loc[:17, ['name', 'cost']]
    inventoryB = wine_info.loc[18:29, ['name', 'cost']]
    inventoryC = wine_info.loc[30:59, ['name', 'cost']]
    
    if code in str(inventoryA.values):
        st.write("**<span style='background-color: #A9D0F5;'>MAERKET A </span>** 에 찾는 와인이 있어용 ~", unsafe_allow_html=True)
        result = inventoryA[inventoryA['name'].str.contains(code)]
        if not result.empty:
            st.write(f"**NAME**: {result.iloc[0]['name']}")

            cost = result.iloc[0]['cost']
            min_cost = float(cost) * mins/100
            min_cost = math.trunc(min_cost)
            min_cost = '{:,}'.format(min_cost)

            max_cost = float(cost) * maxs/100
            max_cost = math.trunc(max_cost)
            max_cost = '{:,}'.format(max_cost)

            cost = '{:,}'.format(cost)
            st.write('**✨BEST PRICE✨ : ₩**', cost)
            st.write('**Online Price Min/Max : ₩**', min_cost, '|', max_cost)

            st.write('---------------------')
        else:
            st.write(f"**No results found for \"{code}\"**")

    if code in str(inventoryB.values):
        st.write("**<span style='background-color: #81BEF7;'>MAERKET B </span>** 에 찾는 와인이 있어용 ~", unsafe_allow_html=True)
        result = inventoryB[inventoryB['name'].str.contains(code)]
        if not result.empty:
            st.write(f"**NAME**: {result.iloc[0]['name']}")
            cost = result.iloc[0]['cost']
            min_cost = float(cost) * mins/100
            min_cost = math.trunc(min_cost)
            min_cost = '{:,}'.format(min_cost)

            max_cost = float(cost) * maxs/100
            max_cost = math.trunc(max_cost)
            max_cost = '{:,}'.format(max_cost)

            cost = '{:,}'.format(cost)
            st.write('**✨BEST PRICE✨ : ₩**', cost)
            st.write('**Online Price Min/Max : ₩**', min_cost, '|', max_cost)
            st.write('---------------------')
        else:
            st.write(f"**No results found for \"{code}\"**")

    if code in str(inventoryC.values):
        st.write("**<span style='background-color: #E3CEF6;'>MAERKET C </span>** 에 찾는 와인이 있어용 ~", unsafe_allow_html=True)
        result = inventoryC[inventoryC['name'].str.contains(code)]
        if not result.empty:
            st.write(f"**NAME**: {result.iloc[0]['name']}")
            cost = result.iloc[0]['cost']
            min_cost = float(cost) * mins/100
            min_cost = math.trunc(min_cost)
            min_cost = '{:,}'.format(min_cost)

            max_cost = float(cost) * maxs/100
            max_cost = math.trunc(max_cost)
            max_cost = '{:,}'.format(max_cost)

            cost = '{:,}'.format(cost)
            st.write('**✨BEST PRICE✨ : ₩**', cost)
            st.write('**Online Price Min/Max : ₩**', min_cost, '|', max_cost)
        else:
            st.write(f"**No results found for \"{code}\"**")


    elif code not in str(inventoryA.values) and code not in str(inventoryB.values) and code not in str(inventoryC.values):
        st.write(f"**No results found for \"{code}\"**")


def page1():

    col1, col2, col3 = st.columns(3)

    n=6

    with col1:

        for i in range(n):
            
            st.write(st.session_state.get('message', ''))

            st.image(wine_info['imgurl'][i], caption=wine_info['name'][i], width = 100)
            st.write('**type** : ', wine_info['type'][i])
            st.write('**city** : ', wine_info['city'][i])
            date = wine_info['name'][i][-4:]
            st.write('**date** :', int(date))
            
            cost = wine_info['cost'][i]
            min_cost = float(cost) * mins/100
            min_cost = math.trunc(min_cost)
            min_cost = '{:,}'.format(min_cost)

            max_cost = float(cost) * maxs/100
            max_cost = math.trunc(max_cost)
            max_cost = '{:,}'.format(max_cost)

            cost = '{:,}'.format(wine_info['cost'][i])
            st.write('**cost : ₩**', cost)
            st.write('**min/max : ₩**', min_cost, '|', max_cost)

        
    with col2:

        for i in range(n, 2*n):
            st.write(st.session_state.get('message', ''))

            st.image(wine_info['imgurl'][i], caption=wine_info['name'][i], width = 100)
            st.write('**type** : ', wine_info['type'][i])
            st.write('**city** : ', wine_info['city'][i])
            date = wine_info['name'][i][-4:]
            st.write('**date** :', int(date))
            
            cost = wine_info['cost'][i]
            min_cost = float(cost) * mins/100
            min_cost = math.trunc(min_cost)
            min_cost = '{:,}'.format(min_cost)

            max_cost = float(cost) * maxs/100
            max_cost = math.trunc(max_cost)
            max_cost = '{:,}'.format(max_cost)

            cost = '{:,}'.format(wine_info['cost'][i])
            st.write('**cost : ₩**', cost)
            st.write('**min/max : ₩**', min_cost, '|', max_cost)


    with col3:

        for i in range(2*n, 3*n):
            st.write(st.session_state.get('message', ''))

            st.image(wine_info['imgurl'][i], caption=wine_info['name'][i], width = 100)
            st.write('**type** : ', wine_info['type'][i])
            st.write('**city** : ', wine_info['city'][i])
            date = wine_info['name'][i][-4:]
            st.write('**date** :', int(date))
            
            cost = wine_info['cost'][i]
            min_cost = float(cost) * mins/100
            min_cost = math.trunc(min_cost)
            min_cost = '{:,}'.format(min_cost)

            max_cost = float(cost) * maxs/100
            max_cost = math.trunc(max_cost)
            max_cost = '{:,}'.format(max_cost)

            cost = '{:,}'.format(wine_info['cost'][i])
            st.write('**cost : ₩**', cost)
            st.write('**min/max : ₩**', min_cost, '|', max_cost)
    if st.button('뒤로가기'):
        st.session_state['main_page'] = 'main_page'


def page2():
    
    col1, col2, col3 = st.columns(3)

    n=4

    with col1:

        for i in range(18 , 18 + 1*n):
            
            st.write(st.session_state.get('message', ''))

            st.image(wine_info['imgurl'][i], caption=wine_info['name'][i], width = 100)
            st.write('**type** : ', wine_info['type'][i])
            st.write('**city** : ', wine_info['city'][i])
            date = wine_info['name'][i][-4:]
            st.write('**date** :', int(date))
            
            cost = wine_info['cost'][i]
            min_cost = float(cost) * mins/100
            min_cost = math.trunc(min_cost)
            min_cost = '{:,}'.format(min_cost)

            max_cost = float(cost) * maxs/100
            max_cost = math.trunc(max_cost)
            max_cost = '{:,}'.format(max_cost)

            cost = '{:,}'.format(wine_info['cost'][i])
            st.write('**cost : ₩**', cost)
            st.write('**min/max : ₩**', min_cost, '|', max_cost)

        
    with col2:

        for i in range(18 + 1*n, 18 + 2*n):
            st.write(st.session_state.get('message', ''))

            st.image(wine_info['imgurl'][i], caption=wine_info['name'][i], width = 100)
            st.write('**type** : ', wine_info['type'][i])
            st.write('**city** : ', wine_info['city'][i])
            date = wine_info['name'][i][-4:]
            st.write('**date** :', int(date))
            
            cost = wine_info['cost'][i]
            min_cost = float(cost) * mins/100
            min_cost = math.trunc(min_cost)
            min_cost = '{:,}'.format(min_cost)

            max_cost = float(cost) * maxs/100
            max_cost = math.trunc(max_cost)
            max_cost = '{:,}'.format(max_cost)

            cost = '{:,}'.format(wine_info['cost'][i])
            st.write('**cost : ₩**', cost)
            st.write('**min/max : ₩**', min_cost, '|', max_cost)


    with col3:

        for i in range(18 + 2*n, 18 + 3*n):
            st.write(st.session_state.get('message', ''))

            st.image(wine_info['imgurl'][i], caption=wine_info['name'][i], width = 100)
            st.write('**type** : ', wine_info['type'][i])
            st.write('**city** : ', wine_info['city'][i])
            date = wine_info['name'][i][-4:]
            st.write('**date** :', int(date))
            
            cost = wine_info['cost'][i]
            min_cost = float(cost) * mins/100
            min_cost = math.trunc(min_cost)
            min_cost = '{:,}'.format(min_cost)

            max_cost = float(cost) * maxs/100
            max_cost = math.trunc(max_cost)
            max_cost = '{:,}'.format(max_cost)

            cost = '{:,}'.format(wine_info['cost'][i])
            st.write('**cost : ₩**', cost)
            st.write('**min/max : ₩**', min_cost, '|', max_cost)

    if st.button('뒤로가기'):
        st.session_state['main_page'] = 'main_page'


def page3():
    col1, col2, col3 = st.columns(3)

    n=10

    with col1:

        for i in range(30 , 30 + 1*n):
            
            st.write(st.session_state.get('message', ''))

            st.image(wine_info['imgurl'][i], caption=wine_info['name'][i], width = 100)
            st.write('**type** : ', wine_info['type'][i])
            st.write('**city** : ', wine_info['city'][i])
            date = wine_info['name'][i][-4:]
            st.write('**date** :', int(date))
            
            cost = wine_info['cost'][i]
            min_cost = float(cost) * float(min_price_range[select])/100
            min_cost = math.trunc(min_cost)
            min_cost = '{:,}'.format(min_cost)

            max_cost = float(cost) * float(max_price_range[select])/100
            max_cost = math.trunc(max_cost)
            max_cost = '{:,}'.format(max_cost)

            cost = '{:,}'.format(wine_info['cost'][i])
            st.write('**cost : ₩**', cost)
            st.write('**min/max : ₩**', min_cost, '|', max_cost)

        
    with col2:

        for i in range(30 + 1*n, 30 + 2*n):
            st.write(st.session_state.get('message', ''))

            st.image(wine_info['imgurl'][i], caption=wine_info['name'][i], width = 100)
            st.write('**type** : ', wine_info['type'][i])
            st.write('**city** : ', wine_info['city'][i])
            date = wine_info['name'][i][-4:]
            st.write('**date** :', int(date))
            
            cost = wine_info['cost'][i]
            min_cost = float(cost) * mins/100
            min_cost = math.trunc(min_cost)
            min_cost = '{:,}'.format(min_cost)

            max_cost = float(cost) * maxs/100
            max_cost = math.trunc(max_cost)
            max_cost = '{:,}'.format(max_cost)

            cost = '{:,}'.format(wine_info['cost'][i])
            st.write('**cost : ₩**', cost)
            st.write('**min/max : ₩**', min_cost, '|', max_cost)


    with col3:

        for i in range(30 + 2*n, 30 + 3*n):
            st.write(st.session_state.get('message', ''))

            st.image(wine_info['imgurl'][i], caption=wine_info['name'][i], width = 100)
            st.write('**type** : ', wine_info['type'][i])
            st.write('**city** : ', wine_info['city'][i])
            date = wine_info['name'][i][-4:]
            st.write('**date** :', int(date))
            
            cost = wine_info['cost'][i]
            min_cost = float(cost) * mins/100
            min_cost = math.trunc(min_cost)
            min_cost = '{:,}'.format(min_cost)

            max_cost = float(cost) * maxs/100
            max_cost = math.trunc(max_cost)
            max_cost = '{:,}'.format(max_cost)

            cost = '{:,}'.format(wine_info['cost'][i])
            st.write('**cost : ₩**', cost)
            st.write('**min/max : ₩**', min_cost, '|', max_cost)

    if st.button('뒤로가기'):
        st.session_state['main_page'] = 'main_page'


st.session_state.setdefault('main_page', 'main_page')

if st.session_state['main_page'] == 'main_page':
    main_page()
elif st.session_state['main_page'] == 'page1':
    page1()
elif st.session_state['main_page'] == 'page2':
    page2()
elif st.session_state['main_page'] == 'page3':
    page3()

