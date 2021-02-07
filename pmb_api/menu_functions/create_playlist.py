from sql_db.extract_db.extract_db import prediction_extract
from pmb_api.get_prediction import *
from spotify_api.pl_builder.get_playlist import *
from spotify_api.playlist_functions.link_validator import link_validator

def create_playlist(st):
    # User input the Spotify Playlist (Implement defensive programming)
    playlist = st.text_input('Insert your Spotify playlist here')
    if playlist != '':
        # Check if the given link is valid
        if link_validator(playlist) == 'Yes':
            st.success('Gotcha!')
        else:
            st.error("That's not a valid link!")

    # User chooses either to use the current prediction or perform a new one
    # Get the current prediction and its date
    current_pred, current_pred_date = prediction_extract()

    # User Selector
    sel_prediction = st.selectbox('Select the prediction:', ['', f'Use current ({current_pred_date})', 'Make a new prediction'])
    
    if sel_prediction == '':
        prediction = None
    
    if sel_prediction == f'Use current ({current_pred_date})':
        st.success('Using current prediction')
        prediction = current_pred
        
        # Plotter
        fig, ax = plt.subplots(figsize=(18,10))
        ax = sns.lineplot(x='pred_min', y='pred_bpm', data=prediction)
        st.pyplot(fig)
    
    elif sel_prediction == 'Make a new prediction':
        fig, prediction = get_prediction(st)
        st.pyplot(fig)
    
    # Call to create the playlist
    if st.button('Create Playlist'):
        get_playlist(playlist, prediction)