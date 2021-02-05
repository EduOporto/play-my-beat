from sql_db.extract_db.extract_db import *
import matplotlib.pyplot as plt 
import seaborn as sns

def show_last_wk(st):
    # Get the last 10 or less workouts and its dates
    last_workouts = heart_rate_extract()
    dates = sorted(list(last_workouts.date.value_counts().index))

    # Build the Streamlit multiselect with all the possible selections to filter the plot
    selector = st.multiselect('Dates', dates, dates)
    
    # Dataframe with the filter implemented
    selected_df = last_workouts[last_workouts.date.isin(selector)]

    # Plotter
    fig, ax = plt.subplots(figsize=(18,10))
    ax = sns.lineplot(x='min', y='bpm', hue='date', data=selected_df)

    return fig