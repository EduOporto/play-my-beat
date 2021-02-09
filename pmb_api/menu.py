import streamlit as st

from pmb_api.menu_functions.update_wk import update_wk
from pmb_api.menu_functions.show_last_wk import show_last_wk
from pmb_api.menu_functions.get_prediction import get_prediction
from pmb_api.menu_functions.create_playlist import create_playlist

def menu():

    radio = st.sidebar.radio('Options', ['Home', 'Update Workouts', 'Show last workouts data', 'Get Prediction', 'Create Playlist'])

    if radio == 'Home':
        st.title('Home')
        st.write("Welcome to the Play My Beat Web APP. With this APP you will be able to sort Spotify Playlists in a way that they will be synched with your heart rate during your exercise.")
        st.write("How is so? You just have to follow the path the options menu shows on the left.")
        st.write("- Update Workouts: this will check your Google Fit data in order to find some new workouts not added to the databases. This will look for workouts since the number of days ago you point on the slider.\nIf some are found, they will be uploaded to the database with its dates, the heart BPM registred for each of the minutes of the workout, and some other data such as calories burned, cadence and distance.")                
        st.write("- Show last workouts data: this plots the data of up to the last 10 workouts. You can select or unselect those workouts in order for they to appear or not on the plot as you wish.")                
        st.write("- Get prediction: automatically builds a new prediction, plotting it below when it is ready.")                
        st.write("- Create a playlist: the flagship of the project. Paste your favourite Spotify playlist's URI, choose if either you want to use the actual prediction or make a new one, press the button and... DONE! Your playlist will appear sorted in your Spotify account.")                
        st.write("Just try!")

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
