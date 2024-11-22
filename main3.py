#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:18:24 2024

@author: selammahmudali
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 14:26:15 2024

@author: selammahmudali
"""

from dataframe import load_movie_data
from quiz_generator_3 import generate_quiz
from performance_tracker3 import PerformanceTracker
import matplotlib.pyplot as plt

def plot_performance(correct, incorrect):
    # Data
    categories = ['Correct', 'Incorrect']
    values = [correct, incorrect]

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(8, 5))

    # Create bar plot
    ax.bar(categories, values, color=['green', 'red'], edgecolor='black')

    # Customize the plot
    ax.set_title('Quiz Performance: Correct vs Incorrect')
    ax.set_ylabel('Number of Answers')
    ax.set_ylim(0, max(values) + 1)  # Set y-axis limit for better visibility

    # Display the plot
    plt.grid(axis='y')  # Add grid lines for better readability
    plt.show()

def main():
    df = load_movie_data()

    # Initialize performance tracker
    tracker = PerformanceTracker()

    print("Welcome to the Movie Quiz!")
    
    # Validate difficulty input
    difficulty = ""
    while difficulty not in ["easy", "medium", "hard"]:
        difficulty = input("Select difficulty (easy, medium, hard): ").lower()
        if difficulty not in ["easy", "medium", "hard"]:
            print("Invalid difficulty. Please choose 'easy', 'medium', or 'hard'.")

    while True:
        # Generate a quiz
        quiz = generate_quiz(difficulty)
        print("\n" + quiz["question"])
        for i, option in enumerate(quiz["options"], 1):
            print(f"{i}. {option}")
        
        # Validate user answer input
        user_answer = None
        while user_answer not in range(1, 5):
            try:
                user_answer = int(input("Your choice (1-4): "))
                if user_answer not in range(1, 5):
                    print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")

        # Check if the answer is correct
        correct = quiz["options"][user_answer - 1] == quiz["answer"]
        print("Correct!" if correct else f"Wrong! The answer was: {quiz['answer']}")

        # Update performance
        tracker.update_score(correct, difficulty)

        while True:
            cont = input("Do you want to continue? (yes/no): ").lower()
            if cont == "yes":
                break  # Exit the prompt loop and immediately return to the quiz
            elif cont == "no":
                # Exit the loop and proceed to show the summary
                summary = tracker.get_summary()
                correct_answers = summary['correct_answers']
                incorrect_answers = summary['total_questions'] - correct_answers
                
                print(f"\nQuiz Completed! You answered {correct_answers} out of {summary['total_questions']} questions correctly.")
                print(f"Your total score: {summary['score']}")
        
                # Plot performance
                plot_performance(correct_answers, incorrect_answers)
                return  # End the quiz function entirely
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
    