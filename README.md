# Play My Beat APP

Every day the number of people that includes any kind of sports wokout on their daily routine increases, and so it does the number of those who add some music to accompany this activities. 

Experts believe that listen a good playlist while exercising can reduce the effects of fatigue by up to 10%, besides the distraction it provides in case of repetitive exercise and the improvement mood can experience.

Not only this: according to an [article](https://www.health.harvard.edu/heart-health/tuning-in-how-music-may-affect-your-heart) published by Harvard University, music can also alter your brain chemistry, producing cardiovascular benefits like enabling to exercise longer during cardiac stress, improve blood vessel function or help heart rate and blood pressure levels to return to baseline more quickly.

![pic_3](img/1_4O7QS_y1Bs6sl-kWXwjjtg.jpeg)

In spirit of those ideas, I felt the need of going one step ahead and ask myself how would it be if both music and exercise where merge together and synchronised. That is why I started to develop this project, with the idea of building and APP that joins the heart BPM collected by any kind of wearable (in my case a Xiaomi Mi Band 3) and stored in the Google Fit app, with the Spotify playlists you use when performing any kind of activity (in my case running).

The idea is to build an APP able to collect that heart performance data registred during any kind of activity and, with it, being able to make a prediction of how the heart is going to perform on the next activity.

Given that prediction, and a Spotify Playlist selected by the user as the playlist he/she will listen during the exercise, sort it in a way that it will be synchronised with that predicted Heart Rates (I will explain how this sortage works few lines below).

## Connecting the parts

Given the latter, I proceed to enumerate the different parts this project will involve:
 
 - [Google Fit API](https://developers.google.com/fit): service connected to the Google Fit APP (available for Android and iOS devices) that makes the insights collected by all the devices (such as smartphones or wearables) registered within the APP available for any registered app project such as this one. It only needs the user authorization for the different data needed.

 - [Spotify API](https://developer.spotify.com/documentation/web-api/): a complete REST service provided by the music streaming platform, which allows to get any kind of information about tracks, artists, playlists and so on, besides giving the possibility to any registered project/app of create and send new playlists to the its users, and even control their playbacks (it will not be the case for this project).

 - [K-Nearest Neighbors Regression](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor): in order to merge the data from the latter two points, this project will try to predict a possible heart performance for the user's next workouts, based on the data collected from the last registered workouts (in this case it will use the last 10 runs registered with the Xiaomi Mi Band 3, this may be improved in the future, in order to accept other kind of activities and devices).

 - SQL Database: all the data will be stored on a SQL database that follows a diagram like the one showed below.

    ![pic4](img/db_diagram.png)

## Run of the application

In order to make the service more accesible I created a quick web app using the Python Library [Streamlit](https://www.streamlit.io/), although my idea is develop a full API service with Flask and some HTML code in the future. An example of the use of this APP is shown on a video below.

[![video_example](img/video.png)](https://youtu.be/VE3zMjKJpnI)

*For the moment I am the only one able to use it, as this project needs client secrets of each of the APIs it uses (Google Fit and Spotify). Anyway, I am trying to approach ways of making it accessible to the final user.*

In order to run the whole APP with Streamlit is necessary to execute the following command on the terminal

    streamlit run login.py

## Deep explaination

### K-Nearest Neighbors Regression 

This model of regression predicts a *y* value of a given *X* based on the training values of the *K* closer (on euclidean distance on the axis) points to that *X* value. Is a non-parametric method that, in an intuitive manner, approximates the association between independent variables *X* and the continuous outcome *y* by averaging the observations in the same neighbourhood. The size of that neighbourhood is set by the *K* value.

In case of this APP, that value is sat in 4, so it takes the four closest values. The rest of the parameters of the model are sat by performing a Grid Search with Cross Validation. This way I get reasonable predictions like the one showed below.

![pic5](img/prediction_example.png)

### Music Selection   
 
Having the tempos of the songs and the mean length of the playlist, the program will divide the heart performance prediction by periods, each of it with a length equal to the mean length of the given playlist, and will stablish an interval of 3 BPM greater and smaller than the Heart BPM's predicted for that period. 
    
With those boundaries stablished, the program will loop through the playlist, finding and storing the songs that fit for the different periods. Once the songs have been listed, one of them will be choosen at random, stored in definitive list and taken away from the original list (in order to avoid repetition). 

Same process will be repeated until all the periods have two songs assigned (I decided to assign two songs per period in order to sort enough songs for a typical workout. If the prediction for the next workout has a length of 40 minutes, the program will sort enough songs for double that length.). 

In case this did not happen with the interval [-3, BPM Prediction, +3], this range will be increased by 3, over and over until all the periods have its two songs assigned. Once this operation have succesfully been performed, the first assigned song of each of the periods will be listed first, then the second song of each of the periods. Both lists will be joined, and the leftovers of the given playlist will be placed right after this two lists.

## Further improvements

 - Implement options for the user to choose the kind of activity he/she would like to get the data from (for the momment it takes data from running activities).
 - Make the APP available at user level, improving the way of saving user's data and client secrets/tokens on the Databases.
 - Build a proper API service with Flask and some HTML code, so it improves the user experience and makes the login/logout tasks more useful.