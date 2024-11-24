#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 19:44:59 2024

@author: selammahmudali
"""

import pandas as pd
import random
import numpy as np  
from dataframe import load_movie_data

def generate_quiz(difficulty):
    """Generates a quiz question based on the specified difficulty."""
    # Load the dataset
    df = load_movie_data()
    
    # Adjust difficulty
    if difficulty == "medium":
        selected_movie = df.sample(1).iloc[0]
        question = f"Who directed the movie '{selected_movie['Series_Title']}'?"
        correct_answer = selected_movie['Director']
        
        # Use numpy to generate unique random options
        all_directors = df["Director"].unique()
        options = np.random.choice(all_directors[all_directors != correct_answer], 3, replace=False).tolist()
        options.append(correct_answer)
        np.random.shuffle(options)  # Shuffle options
    
    elif difficulty == "easy":
        selected_movie = df.sample(1).iloc[0]
        question = f"Which actor starred in '{selected_movie['Series_Title']}'?"
        correct_answer = selected_movie['Star1'] or selected_movie['Star2'] or selected_movie['Star3'] or selected_movie['Star4']
        
        # Use numpy for generating random actor options
        all_actors = df['Star1'].dropna().unique()  # Get unique non-NaN actors
        options = np.random.choice(all_actors[all_actors != correct_answer], 3, replace=False).tolist()
        options.append(correct_answer)
        np.random.shuffle(options)
    
    elif difficulty == "hard":
        selected_movie = df.sample(1).iloc[0]
        question = f"What year was the movie '{selected_movie['Series_Title']}' released?"
        correct_answer = selected_movie['Released_Year']
        
        # Use numpy to pick random years
        all_years = df["Released_Year"].unique()
        options = np.random.choice(all_years[all_years != correct_answer], 3, replace=False).tolist()
        options.append(correct_answer)
        np.random.shuffle(options)
    
    return {
        "question": question,
        "options": options,
        "answer": correct_answer
    }
