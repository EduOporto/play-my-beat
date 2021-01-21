import requests
from bs4 import BeautifulSoup
import pandas as pd

types_web = requests.get('https://developers.google.com/fit/rest/v1/reference/activity-types')
soup = BeautifulSoup(types_web.text, features="html.parser")

headers = [e.text for e in soup.find_all('th')]
data = [e.text for e in soup.find_all('td')]

types = [e for e in data if data.index(e)%2 == 0]
values = [int(e) for e in data if data.index(e)%2 != 0]

df = pd.DataFrame({headers[0]:types, headers[1]:values})

def types_df(value, df=df):
    if value != 72:
        return df[df['Integer Value'] == value]['Activity Type'].to_list()[0]
    else:
        return 'Sleep'
