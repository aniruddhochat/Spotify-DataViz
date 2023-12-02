# %%
import config as c
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

df = pd.read_csv('spotifyFinal.csv')
st.title("Genre-wise Popularity Over Years")
selected_genre = st.multiselect("Select Genre", df['Genre'].unique())
filtered_df = df[df['Genre'].isin(selected_genre)]
genre_year_popularity = filtered_df.groupby(['Genre', 'Year']).agg({'Popularity': 'mean'}).reset_index()
fig = px.line(genre_year_popularity, x='Year', y='Popularity', color='Genre', markers=True, title='Genre-wise Popularity Over Years')
fig.update_layout(xaxis_title='Release Years', yaxis_title='Average Popularity')
st.plotly_chart(fig)


st.title('Top 5 Artists Every Year Based on Popularity')
selected_year = st.sidebar.selectbox('Select Year', df['Year'].unique())
yeardf = df[df['Year'] == selected_year]
#artist_popularity = yeardf.groupby('Artist')['Popularity'].mean().sort_values(ascending=False)
artist_popularity = yeardf.groupby(['Artist']).agg({'Popularity': 'mean'}).sort_values(by='Popularity',ascending=False).reset_index()
barfig = px.bar(artist_popularity, x=artist_popularity['Artist'], y=artist_popularity['Popularity'], title=f'Top 5 Artists in {selected_year}', labels={'Popularity': 'Average Popularity'})
st.plotly_chart(barfig)