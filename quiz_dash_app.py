#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 14:49:23 2024

@author: selammahmudali
"""

from dash import Dash, html, dcc, Input, Output, State, callback_context
import random
import plotly.graph_objects as go
from dataframe import load_movie_data
from quiz_generator_3 import generate_quiz
from performance_tracker3 import PerformanceTracker

# Load movie data
df = load_movie_data()

# Initialize performance tracker
tracker = PerformanceTracker()

# Create Dash app
app = Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1("Movie Quiz", style={'textAlign': 'center'}),
    html.Div([
        html.Label("Select Difficulty:"),
        dcc.Dropdown(
            id="difficulty-dropdown",
            options=[
                {"label": "Easy", "value": "easy"},
                {"label": "Medium", "value": "medium"},
                {"label": "Hard", "value": "hard"},
            ],
            value="easy",
            placeholder="Select difficulty"
        ),
    ], style={'width': '50%', 'margin': '0 auto'}),

    html.Div(id="quiz-container", children=[
        html.H3(id="quiz-question", style={'marginTop': '20px'}),
        dcc.RadioItems(
            id="quiz-options",
            options=[],
            style={'margin': '20px 0'}
        ),
        html.Button("Submit Answer", id="submit-btn", n_clicks=0),
        html.Div(id="quiz-feedback", style={'marginTop': '20px', 'color': 'blue'}),
        html.Div(children=[
            html.Button("Continue", id="continue-btn", n_clicks=0, style={'marginRight': '10px'}),
            html.Button("End Quiz", id="end-btn", n_clicks=0),
        ], style={'marginTop': '20px', 'display': 'none'}, id="continue-end-container"),
    ], style={'textAlign': 'center', 'display': 'none'}),

    html.Div(id="summary-container", style={'textAlign': 'center', 'display': 'none'}, children=[
        html.H2("Quiz Summary"),
        html.Div(id="quiz-summary"),
        dcc.Graph(id="performance-plot"),
        html.Button("Restart Quiz", id="restart-btn", n_clicks=0)
    ]),

    html.Div(id="quiz-control-container", style={'textAlign': 'center', 'marginTop': '20px'}, children=[
        html.Button("Start Quiz", id="start-btn", n_clicks=0)
    ])
])

# Global variable to store the current quiz question
current_quiz = None
quiz_difficulty = "easy"

@app.callback(
    [
        Output("quiz-container", "style"),
        Output("quiz-question", "children"),
        Output("quiz-options", "options"),
        Output("quiz-feedback", "children"),
        Output("continue-end-container", "style"),
        Output("summary-container", "style"),
        Output("quiz-summary", "children"),
        Output("performance-plot", "figure"),
        Output("quiz-control-container", "style"),
    ],
    [
        Input("start-btn", "n_clicks"),
        Input("submit-btn", "n_clicks"),
        Input("continue-btn", "n_clicks"),
        Input("end-btn", "n_clicks"),
        Input("restart-btn", "n_clicks"),
    ],
    [
        State("difficulty-dropdown", "value"),
        State("quiz-options", "value"),
    ],
    prevent_initial_call=True
)
def handle_all_triggers(start_clicks, submit_clicks, continue_clicks, end_clicks, restart_clicks, difficulty, selected_option):
    global current_quiz, quiz_difficulty
    ctx = callback_context
    triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]

    # Handle "Start Quiz" button
    if triggered_id == "start-btn":
        quiz_difficulty = difficulty
        current_quiz = generate_quiz(quiz_difficulty)
        question = current_quiz["question"]
        options = [{"label": opt, "value": opt} for opt in current_quiz["options"]]
        return (
            {'display': 'block'},  # Show quiz-container
            question,
            options,
            "",  # Clear feedback
            {'display': 'none'},  # Hide continue/end buttons initially
            {'display': 'none'},  # Hide summary-container
            "",  # Clear summary
            go.Figure(),  # Empty plot
            {'display': 'none'}  # Hide quiz-control-container
        )

    # Handle "Submit Answer" button
    if triggered_id == "submit-btn" and selected_option:
        correct = selected_option == current_quiz["answer"]
        tracker.update_score(correct, quiz_difficulty)
        feedback = "Correct!" if correct else f"Wrong! The answer was: {current_quiz['answer']}"
        return (
            {'display': 'block'},  # Keep showing quiz-container
            current_quiz["question"],
            [{"label": opt, "value": opt} for opt in current_quiz["options"]],
            feedback,
            {'display': 'block'},  # Show continue/end buttons
            {'display': 'none'},  # Hide summary-container
            "",  # Clear summary
            go.Figure(),  # Empty plot
            {'display': 'none'}  # Hide quiz-control-container
        )

    # Handle "Continue" button
    if triggered_id == "continue-btn":
        current_quiz = generate_quiz(quiz_difficulty)
        question = current_quiz["question"]
        options = [{"label": opt, "value": opt} for opt in current_quiz["options"]]
        return (
            {'display': 'block'},  # Show quiz-container
            question,
            options,
            "",  # Clear feedback
            {'display': 'none'},  # Hide continue/end buttons
            {'display': 'none'},  # Hide summary-container
            "",  # Clear summary
            go.Figure(),  # Empty plot
            {'display': 'none'}  # Hide quiz-control-container
        )

    # Handle "End Quiz" button
    if triggered_id == "end-btn":
        summary = tracker.get_summary()
        correct_answers = summary['correct_answers']
        total_questions = summary['total_questions']
        incorrect_answers = total_questions - correct_answers

        # Generate performance plot
        fig = go.Figure()
        fig.add_trace(go.Bar(x=['Correct', 'Incorrect'], y=[correct_answers, incorrect_answers],
                             marker_color=['green', 'red']))
        fig.update_layout(
            title="Quiz Performance: Correct vs Incorrect",
            xaxis_title="Category",
            yaxis_title="Number of Answers",
            barmode="group"
        )

        summary_text = f"""
            Quiz Completed! You answered {correct_answers} out of {total_questions} questions correctly.
            Your total score: {summary['score']}
        """
        return (
            {'display': 'none'},  # Hide quiz-container
            "",  # Clear question
            [],  # Clear options
            "",  # Clear feedback
            {'display': 'none'},  # Hide continue/end buttons
            {'display': 'block'},  # Show summary-container
            summary_text,
            fig,
            {'display': 'none'}  # Hide quiz-control-container
        )

    # Handle "Restart Quiz" button
    if triggered_id == "restart-btn":
        tracker.reset()
        return (
            {'display': 'none'},  # Hide quiz-container
            "",  # Clear question
            [],  # Clear options
            "",  # Clear feedback
            {'display': 'none'},  # Hide continue/end buttons
            {'display': 'none'},  # Hide summary-container
            "",  # Clear summary
            go.Figure(),  # Empty plot
            {'display': 'block'}  # Show quiz-control-container
        )


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
