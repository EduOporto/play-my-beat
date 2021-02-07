from sql_db.update_db.update_db import prediction_update
import matplotlib.pyplot as plt 
import seaborn as sns

def get_prediction(st):
    # Get new prediction
    with st.spinner('Building the model and the prediction...'):
        prediction, message = prediction_update()

    # Plotter
    fig, ax = plt.subplots(figsize=(18,10))
    ax = sns.lineplot(x='min', y='bpm', data=prediction)

    # Message
    st.success(message)

    return fig, prediction
