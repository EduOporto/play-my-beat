import pmb_api.SessionState as SState
from pmb_api.menu import menu
import streamlit as st

st.sidebar.header('User Login')

state = SState.get(key=0)

usr_placeholder = st.sidebar.empty()
pwd_placeholder = st.sidebar.empty()

if st.sidebar.button('LogOut'):
    state.key += 1

usr_value = usr_placeholder.text_input("Username", '', key=state.key)
pwd_value = pwd_placeholder.text_input("Password", '', type='password', key=state.key)

if usr_value == 'admin' and pwd_value == 'admin':
    menu()