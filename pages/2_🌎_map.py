import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium, folium_static
import random
import math


i=0
wine_info = pd.read_csv('./vivino_dataset_0417.csv')

# 10
max_price_range = [99.5, 99.8, 99.7, 99.6, 99.5, 99.4, 99.3, 99.1, 99]
min_price_range = [98.9, 98.7, 98.3, 98, 97.8, 96, 95, 94, 90]

select = random.randrange(0, 10)
def main_page():
    global i

    with st.container():
        st.title('Which wine are you looking for?🍷')

        code = st.text_input(
            'Search anything!',
            value='',
            placeholder='Wine'
        )    ##### 여기서 입력값 받아와야함!!! 입력값 -> code


        st.text(' ')
        st.text(' ')

        col_map, col_des = st.columns([4,1])

    with col_map:
        m = folium.Map(location=[35.228956, 126.843181], zoom_start=16)
        folium.Marker(
            [35.228956, 126.843181],
            popup='GIST',
            tooltip='Dasan'
        ).add_to(m)
        
        inventory=''
        for i in range(18) : 
            inventory = inventory + wine_info['name'][i] + '\n - '

        markerA = folium.Marker(
            [35.22115148181801, 126.84508234413954],
            popup=folium.Popup(inventory[:-2], max_width=250),
            tooltip='MARKET A'
        ).add_to(m)

        markerB = folium.Marker(
            [35.22359306367261, 126.85141562924461],
            popup=folium.Popup("매장재고!", max_width=300),
            tooltip='MARKET B'
        ).add_to(m)

        markerC = folium.Marker(
            [35.221234713907336, 126.8540341090701],
            popup=folium.Popup("매장재고!", max_width=300),
            tooltip='MARKET C'
        ).add_to(m)

        folium.Marker(
            location=[35.234738, 126.838680],
            icon=folium.Icon(color="red"),
            popup=folium.Popup("I'm a red marker", max_width=300),
            tooltip='Red Marker'
        ).add_to(m)

        st_data = st_folium(m, width=725)

    with col_des:
        df = pd.DataFrame(
        [
            {"command": "st.selectbox", "rating": 4, "is_widget": True},
            {"command": "st.balloons", "rating": 5, "is_widget": False},
            {"command": "st.time_input", "rating": 3, "is_widget": True},
        ]
        )
        edited_df = st.experimental_data_editor(df, num_rows="dynamic")

        favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
        st.markdown(f"Your choices are **{favorite_command}** 🍷")


    st.title('와인 매장을 보여드릴게요 🐾')

    st.session_state.setdefault('main_page', 'main_page')
        
    if st.button('MARKET A'):
        st.session_state['main_page'] = 'page1'
            
    if st.button('MARKET B'):
        st.session_state['main_page'] = 'page2'

    if st.button('MARKET C'):
        st.session_state['main_page'] = 'page3'


def page1():

    col1, col2, col3 = st.columns(3)

    global i
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

        for i in range(n, 2*n):
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


    with col3:

        for i in range(2*n, 3*n):
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

    if st.button('뒤로가기'):
        st.session_state['main_page'] = 'main_page'

def page2():
    st.title('와인 2')
    st.write(st.session_state.get('message', ''))
    if st.button('뒤로가기'):
        st.session_state['main_page'] = 'main_page'

def page3():
    st.title('와인 3')
    st.write(st.session_state.get('message', ''))
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