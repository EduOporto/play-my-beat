import datetime

def activity_merger(sessions):
    # Put on a column aside the date of each of the workouts (with no time)
    sessions['justDate'] = sessions.startDate.apply(lambda x: x.date())

    # Get the value counts of the new column, if one of the dates have more than one value, work on this
    date_counts = sessions.justDate.value_counts()
    
    # List to append the indexes of the repeated workouts, in order to delete them from the dataframe
    to_drop = []

    for index, row in date_counts.items():
        if row > 1:
            # Get the date with more than one workout 
            day = sessions[sessions.justDate == index]

            # Get the starts and ends of each of the workouts on separated lists, with its indexes
            starts = []
            ends = []

            for index, row in day.iterrows():
                starts.append((index, row.startDate))
                ends.append((index, row.endDate))

            # Delete the start of the first workout and the end of the last workout, in order to
            # calculate the gaps between workouts
            starts = starts[1:]
            ends = ends[:-1]

            # Calculate the gaps between the start of the next workout and the end of the past one
            # If it is smaller than 10 minutes, this means there was an issue while tracking the activity,
            # but the data belongs to the same activity, so the indexes of both activities will be added
            # to the list of activities to be merged
            to_merge = []

            for start, end in zip(starts, ends):
                if start[1] - end[1] < datetime.timedelta(0, 600):
                    to_merge.append(start[0])
                    to_merge.append(end[0])
                    
            to_merge = list(set(to_merge))
            to_merge.sort()
            
            # Sort the selected indexes from smaller to greater, so the new 'workout' can select the startDate 
            # of the erliest registred workout (the smallest index) and the endDate of the latest (the greatest
            # index)
            if len(to_merge) > 0:
                # Append the indexes to the list for the posterior droppage
                to_drop.append(to_merge)
                
                # Get the index of the first and last workouts, in order to merge them
                new_row_start = to_merge[0]
                new_row_end = to_merge[-1]

                # Build the new row and append it to the workouts dataframe
                new_row = {'activityType': sessions.iloc[new_row_start].activityType,
                           'startDate': sessions.iloc[new_row_start].startDate,
                           'startDate_nano': sessions.iloc[new_row_start].startDate_nano,
                           'endDate': sessions.iloc[new_row_end].endDate,
                           'endDate_nano': sessions.iloc[new_row_end].endDate_nano,
                           'packName': sessions.iloc[new_row_start].packName,
                           'justDate': sessions.iloc[new_row_start].justDate}
                
                sessions = sessions.append(new_row, ignore_index=True) 

            else:
                pass
     
    # Drop the indexes of the splitted workouts, in order to have just the unified workout
    to_drop = [e_1 for e in to_drop for e_1 in e] 
    sessions.drop(to_drop, inplace=True)
    
    # Return the dataset
    return sessions.sort_values('startDate').reset_index(drop=True)
