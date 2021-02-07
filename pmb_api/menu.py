import streamlit as st

from pmb_api.update_wk import update_wk
from pmb_api.show_last_wk import show_last_wk
from pmb_api.get_prediction import get_prediction
from pmb_api.create_playlist import create_playlist

def menu():

    radio = st.sidebar.radio('Options', ['Home', 'Update Workouts', 'Show last workouts data', 'Get Prediction', 'Create Playlist'])

    if radio == 'Home':
        st.title('Home')

    elif radio == 'Update Workouts':
        st.title('Update Workouts')
        update_wk(st)

    elif radio == 'Show last workouts data':
        st.title('Show last workouts data')
        st.pyplot(show_last_wk(st))

    elif radio == 'Get Prediction':
        st.title('Get Prediction')
        fig, prediction = get_prediction(st)
        st.pyplot(fig)

    elif radio == 'Create Playlist':
        st.title('Create Playlist')
        create_playlist(st)
