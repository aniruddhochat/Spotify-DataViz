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
st.title("Genre-wise Popularity Over Years")

# Genre Filter
selected_genre = st.multiselect("Select Genre", df['Genre'].unique())

# Filter DataFrame
filtered_df = df[df['Genre'].isin(selected_genre)]

# # Plot
# fig = px.line(
#     filtered_df,
#     x='Year',
#     y='Popularity',
#     color='Genre',
#     markers=True,
#     title='Genre-wise Popularity Over Years',
# )

# # Update layout for better readability
# fig.update_layout(
#     xaxis_title='Years',
#     yaxis_title='Average Popularity',
#     legend_title='Genre',
#     legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
# )

# # Display Plot
# st.plotly_chart(fig)


genre_year_popularity = filtered_df.groupby(['Genre', 'Year']).agg({'Popularity': 'mean'}).reset_index()

# Plotting
# plt.figure(figsize=(14, 8))
# sns.lineplot(x='Year', y='Popularity', hue='Genre', data=genre_year_popularity, palette='viridis', marker='o')
# plt.title('Genre-wise Popularity Over Years')
# plt.xlabel('Release Years')
# plt.ylabel('Average Rank')
# plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')

# # Display the plot in Streamlit
# st.pyplot(plt)

# plt.figure(figsize=(14, 8))
# sns.lineplot(x='Year', y='Popularity', hue='Genre', data=genre_year_popularity, palette='viridis', marker='o')
# plt.title('Genre-wise Popularity Over Years')
# plt.xlabel('Years')
# plt.ylabel('Average Popularity')
# plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')


genre_month_popularity = filtered_df.groupby(['Genre', 'Year']).agg({'Popularity': 'mean'}).reset_index()
filtered_df.head()
plt.figure(figsize=(14, 8))
sns.lineplot(x='Year', y='Popularity', hue='Genre', data=genre_month_popularity, palette='viridis', marker='o')
plt.title('Genre-wise Popularity Over Years')
plt.xlabel('Years')
plt.ylabel('Average Popularity')
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')

st.pyplot(plt)

fig = px.line(genre_year_popularity, x='Year', y='Popularity', color='Genre', markers=True, title='Genre-wise Popularity Over Years')
fig.update_layout(xaxis_title='Release Years', yaxis_title='Average Popularity')
st.plotly_chart(fig)
# %%



