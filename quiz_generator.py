def generate_quiz(movie_data):    if movie_data:        title = movie_data['title']        year = movie_data['year']        genre = movie_data['genres'][0]  # Assume the first genre is sufficient        # Create a simple question about the movie's year        question = f"In what year was the movie '{title}' released?"        options = [year, year - 1, year + 1, year - 2]        return question, options    else:        return None, None