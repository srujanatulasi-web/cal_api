import streamlit as st
import requests

def get_rooms():
    res = requests.post("http://127.0.0.1:8000/rooms")
    data = res.json()
    return data

def create_room(floorno, roomtype, price, is_booked):
    data = {
        'floor': floorno,
        'price': price,
        'type': roomtype,
        'is_booked': bool(is_booked)
    }
    res = requests.post("http://127.0.0.1:8000/rooms/add",json=data)

@st.dialog("Create Room")
def show_dialog():
    floorno = st.number_input('Floor',min_value=0)
    roomtype = st.selectbox('Type',['Normal','premium','delux'])
    price    = st.text_input('price per day')
    is_booked = st.toggle('Is Booked')
    if st.button('create', type='primary'):
        create_room(floorno, roomtype, price, is_booked)
        st.rerun()

st.title('Booking App')
if st.button('+ add New Room',type='primary'):
    show_dialog()
    



rooms = get_rooms()
st.table(rooms)