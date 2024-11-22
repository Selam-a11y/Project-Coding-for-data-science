#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 19:11:46 2024

@author: selammahmudali
"""

#import numpy as np
import pandas as pd

# These are just some display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# Display floating points in a more readable format
pd.options.display.float_format = '{:,.2f}'.format
# Read in the movies data first
df = pd.read_csv("//Users/selammahmudali/Desktop/CODING PROJECT/imdb_top_1000.csv.xls")


# Extract columns using their indices (0-based indexing)
selected_columns = df.iloc[:, [1, 2, 6, 9, 10, 11, 12, 13]]

# Display the extracted columns
#print(selected_columns)
# data_wrangler.py

#Save the extracted columns to a new CSV file
selected_columns.to_csv("//Users/selammahmudali/Desktop/CODING PROJECT/imdb_top_1000_selected_columns.csv", index=False)

print("New CSV file with selected columns has been created.")


def load_movie_data():
    # Load the dataset and return the DataFrame
    df = pd.read_csv("imdb_top_1000_selected_columns.csv")  # Ensure the path to your CSV is correct
    return df


#print("function Valid")
