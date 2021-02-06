# Play My Beat APP

Every day the number of people that includes any kind of sports wokout on their daily routine increases, and so it does the number of those who add some music to accompany this activities. 

Experts believe that listen a good playlist while exercising can reduce the effects of fatigue by up to 10%, besides the distraction it provides in case of repetitive exercise and the improvement mood can experience.

Not only this: according to an [article](https://www.health.harvard.edu/heart-health/tuning-in-how-music-may-affect-your-heart) published by Harvard University, music can also alter your brain chemistry, producing cardiovascular benefits like enabling to exercise longer during cardiac stress, improve blood vessel function or help heart rate and blood pressure levels to return to baseline more quickly.

![pic_3](img/1_4O7QS_y1Bs6sl-kWXwjjtg.jpeg)

In spirit of those ideas, I felt the need of going one step ahead and ask myself how would it be if both music and exercise where merge together and synchronised. That is why I started to develop this project, with the idea of building and APP that joins the heart BPM collected by any kind of wearable (in my case a Xiaomi Mi Band 3) and stored in the Google Fit app, with the Spotify playlists you use when performing any kind of activity (in my case running).

## Connecting the parts

Given the latter, I proceed to enumerate the different parts this project will involve:
 
 - [Google Fit API](https://developers.google.com/fit): service connected to the Google Fit APP (available for Android and iOS devices) that makes the insights collected by all the devices (such as smartphones or wearables) registered within the APP available for any registered app project such as this one. It only needs the user authorization for the different data needed.

 - [Spotify API](https://developer.spotify.com/documentation/web-api/): a complete REST service provided by the music streaming platform, which allows to get any kind of information about tracks, artists, playlists and so on, besides giving the possibility to any registered project/app of create and send new playlists to the its users, and even control their playbacks (it will not be the case for this project).

 - [K-Nearest Neighbors Regression](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor)): in order to merge the data from the latter two points, this project will try to predict a possible heart performance for the user's next workouts, based on the data collected from the last registered workouts (in this case it will use the last 10 runs registered with the Xiaomi Mi Band 3, this may be improved in the future, in order to accept other kind of activities and devices).

## Run of the application



## Deep explaination

### Time Series Forecasting with SARIMAX

### Music Selection   
 
Having the tempos of the songs and the mean length of the playlist, the program will divide the heart performance prediction by periods, each of it with a length equal to the mean length of the given playlist, and will stablish an interval of 3 BPM greater and smaller than the Heart BPM's predicted for that period. 
    
With those boundaries stablished, the program will loop through the playlist, finding and storing the songs that fit for the different periods. Once the songs have been listed, one of them will be choosen at random, stored in definitive list and taken away from the original list (in order to avoid repetition). 

Same process will be repeated until all the periods have two songs assigned (I decided to assign two songs per period in order to sort enough songs for a typical workout. If the prediction for the next workout has a length of 40 minutes, the program will sort enough songs for double that length.). 

In case this did not happen with the interval [-3, BPM Prediction, +3], this range will be increased by 3, over and over until all the periods have its two songs assigned. Once this operation have succesfully been performed, the first assigned song of each of the periods will be listed first, then the second song of each of the periods. Both lists will be joined, and the leftovers of the given playlist will be placed right after this two lists.

## Further improvements