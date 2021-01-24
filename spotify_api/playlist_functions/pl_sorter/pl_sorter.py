import pandas as pd

def playlist_sorter(run_intervals, playlist_df):
    # Create a dict with each of the intervals as keys and empty lists as values
    range_box = {}
    for i in range(run_intervals.shape[0]):
        range_box[i] = []
    
    # List with the number of elements, in order to control the loop through the songs
    lenght_range_box = list(range(len(range_box)))

    # Accumulator of the ranges. The loop starts with a range of 3 BPM more and less of the predicted BPM 
    # for that interval. After that loop is done, this range increases to 6, 9, 12 and so one, until 
    # the loop has chosen two songs for each of the intervals 
    ranger = 3

    # Once the loop has chosen two song for a given interval, those go to this empty dict and disappear 
    # from 'range_box'
    final_choices = {}

    # This while loop stops when all the intervals have two songs assigned
    while len(lenght_range_box) > 0:
        # Iterating through the time intervals
        for time, ran in zip(run_intervals.iterrows(), lenght_range_box):
            
            # Building the interval
            interval = pd.Interval(left=time[1]['predicted_mean']-ranger,
                                   right=time[1]['predicted_mean']+ranger,
                                   closed='both')
            
            # List of the songs that fit for the BPM interval of the time iterated
            songs_chosen = playlist_df[playlist_df.tempo.between(interval.left, interval.right, inclusive=True)]

            try:
                # If there are songs available, pick a random one, assign it to 'range_box' and drop it 
                # from the song's dataframe
                song = songs_chosen.sample()
                range_box[ran].append(song.uri.values[0])
                playlist_df.drop(song.index[0], inplace=True)                
            except:
                # Pass if there are no songs available
                pass
            
            # Check wether the iterated time interval has been filled with two songs. If so, assign it to
            # the dict of 'final_choices' and drop it from the time_intervals dataframe and the control list
            if len(range_box[ran]) == 2:
                final_choices[ran] = range_box[ran]
                    
                #del range_box[ran] and the time interval
                lenght_range_box.remove(ran)
                run_intervals.drop(time[0], inplace=True)
            
        # Increase the ranges of the BPMs +3
        ranger += 3

    # Sort the results by time intervals, placing the first song of each list first, and the second second.
    # Join both lists and the leftovers of the given playlist at the end
    choice_sorted = sorted(final_choices.items())
    choice_ready = [e[1][0] for e in choice_sorted] + [e[1][1] for e in choice_sorted] + playlist_df.uri.to_list()

    return choice_ready