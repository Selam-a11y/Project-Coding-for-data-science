#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:30:12 2024

@author: selammahmudali
"""

class PerformanceTracker:
    def __init__(self):
        self.correct_answers = 0
        self.total_questions = 0
        self.difficulty_weights = {"easy": 1, "medium": 2, "hard": 3}
        self.score = 0

    def update_score(self, correct, difficulty):
        self.total_questions += 1
        if correct:
            self.correct_answers += 1
            self.score += self.difficulty_weights[difficulty]

    def get_summary(self):
        return {
            "total_questions": self.total_questions,
            "correct_answers": self.correct_answers,
            "score": self.score
        }
import matplotlib.pyplot as plt



def plot_performance(summary):
    """Visualize performance as a pie chart."""
    labels = ['Correct', 'Incorrect']
    values = [summary['correct_answers'], summary['total_questions'] - summary['correct_answers']]
    
    # Create the pie chart
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#4CAF50', '#F44336'])
    ax.axis('equal')  # Equal aspect ratio ensures a perfect circle
    return fig
