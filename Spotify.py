# %%
import config as c
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

# %%
# %%
df = pd.read_csv('spotify.csv')
# df.head()

# %%
df['ReleaseDate'].value_counts()
df = df[~df['ReleaseDate'].isin(['1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2018'])]
df.shape

# %%
# uniqueTracks = df['TrackID'].unique()
# print(len(uniqueTracks))

# %%
df['ReleaseDate'] = pd.to_datetime(df['ReleaseDate'])

# %%
df['Month'] = df['ReleaseDate'].dt.month
df['Year'] = df['ReleaseDate'].dt.year

# %%

# filtered_df = df[(df['ReleaseDate'].dt.year >= 2001) & (df['ReleaseDate'].dt.year <= 2001) & (df['Genre'] == 'big beat')]


# genre_month_popularity = filtered_df.groupby(['Genre', 'Month']).agg({'Popularity': 'mean'}).reset_index()

# plt.figure(figsize=(14, 8))
# sns.lineplot(x='Month', y='Popularity', hue='Genre', data=genre_month_popularity, palette='viridis', marker='o')
# plt.title('Genre-wise Popularity Over Months (2000-2000)')
# plt.xlabel('Month')
# plt.ylabel('Average Popularity')
# plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')

# plt.show()

# %%
# filtered_df = filtered_df.drop(filtered_df.index)

# # %%
# #filtered_df = df[(df['ReleaseDate'].dt.year >= 2001) & (df['ReleaseDate'].dt.year <= 2001) & (df['Genre'] == 'big beat')]
# filtered_df = df[(df['Genre'].isin(['pop','hip hop']))]

# genre_month_popularity = filtered_df.groupby(['Genre', 'Year']).agg({'Popularity': 'mean'}).reset_index()

# plt.figure(figsize=(14, 8))
# sns.lineplot(x='Year', y='Popularity', hue='Genre', data=genre_month_popularity, palette='viridis', marker='o')
# plt.title('Genre-wise Popularity Over Years')
# plt.xlabel('Years')
# plt.ylabel('Average Popularity')
# plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')

# plt.show()

# %%
st.title("Interactive Genre-wise Popularity Over Years")

# Genre Filter
selected_genre = st.multiselect("Select Genre", df['Genre'].unique())

# Filter DataFrame
filtered_df = df[df['Genre'].isin(selected_genre)]

# Plot
fig = px.line(
    filtered_df,
    x='Year',
    y='Popularity',
    color='Genre',
    markers=True,
    title='Genre-wise Popularity Over Years',
)

# Update layout for better readability
fig.update_layout(
    xaxis_title='Years',
    yaxis_title='Average Popularity',
    legend_title='Genre',
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
)

# Display Plot
st.plotly_chart(fig)

# %%



