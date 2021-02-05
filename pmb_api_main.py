import streamlit as st

from pmb_api.update_wk import update_wk
from pmb_api.show_last_wk import show_last_wk

from spotify_api.pl_builder.get_playlist import *
from forecast.k_nearest_n.get_prediction import *


radio = st.sidebar.radio('Options', ['Home', 'User Login', 'Update Workouts', 'Show last workouts data', 'Get Prediction', 'Create Playlist'])

if radio == 'Home':
    st.title('Home')

elif radio == 'User Login':
    st.title('Login')
    pass

elif radio == 'Update Workouts':
    st.title('Update Workouts')
    update_wk(st)

elif radio == 'Show last workouts data':
    st.title('Show last workouts data')
    st.pyplot(show_last_wk(st))

elif radio == 'Get Prediction':
    st.title('Get Prediction')
    # prediction = get_prediction()

elif radio == 'Create Playlist':
    st.title('Create Playlist')
    # get_playlist(playlist_uri, prediction)
