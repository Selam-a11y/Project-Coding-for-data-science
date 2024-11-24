#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:38:47 2024

@author: selammahmudali
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Read in the movies data first
df = pd.read_csv("/Users/selammahmudali/Desktop/Project-Coding-for-data-science/imdb_top_1000.csv.xls")


#1)
#Top 10 Movies by number of Votes

top_voted_movies = df.nlargest(10, 'No_of_Votes')

plt.figure(figsize=(12, 6))
plt.bar(top_voted_movies['Series_Title'], top_voted_movies['No_of_Votes'], color='gold', edgecolor='black')
plt.title('Top 10 Movies by Number of Votes', fontsize=14)
plt.xlabel('Movie Title', fontsize=8)
plt.ylabel('Number of Votes', fontsize=8)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()




#2)
#Top 15 Genrees by IMDb Ratings

# Step 1: Group data by genres and calculate median ratings for sorting
genre_stats = df.groupby('Genre')['IMDB_Rating'].median().sort_values(ascending=False)

# Step 2: Select the top 15 genres based on median ratings
top_15_genres = genre_stats.head(15).index

# Step 3: Filter the dataset to include only the top 15 genres
filtered_data = df[df['Genre'].isin(top_15_genres)]

# Step 4: Create the boxplot
plt.figure(figsize=(12, 8))
sns.boxplot(data=filtered_data, x='Genre', y='IMDB_Rating', palette='Set3', order=top_15_genres)

# Step 5: Customize the plot
plt.title('Top 15 Genres by IMDb Ratings', fontsize=16)
plt.xlabel('Genre', fontsize=12)
plt.ylabel('IMDb Rating', fontsize=12)
plt.xticks(rotation=90, fontsize=10, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()

# Show the plot
plt.show()


