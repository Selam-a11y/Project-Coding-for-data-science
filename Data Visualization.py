#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 11:34:47 2024

@author: selammahmudali
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("/Users/selammahmudali/Desktop/Project-Coding-for-data-science/imdb_top_1000.csv.xls")

# Step 1: Group data by genres and calculate median ratings for sorting
genre_stats = df.groupby('Genre')['IMDB_Rating'].median().sort_values(ascending=False)

# Step 2: Select the top 15 genres based on median ratings
top_15_genres = genre_stats.head(15).index

# Step 3: Filter the dataset to include only the top 15 genres
filtered_data = df[df['Genre'].isin(top_15_genres)]

# Step 4: Create the boxplot
plt.figure(figsize=(12, 8))
sns.boxplot(data=filtered_data, x='Genre', y='IMDB_Rating', order=top_15_genres)

# Step 5: Customize the plot
plt.title('Top 15 Genres by IMDb Ratings', fontsize=16)
plt.xlabel('Genre', fontsize=12)
plt.ylabel('IMDb Rating', fontsize=12)
plt.xticks(rotation=90, fontsize=10, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()

# Show the plot
plt.show()
