import pandas as pd
import numpy as np
import sqlite3


def fetch_data(query):
    """Fetch data from the SQLite database."""
    conn = sqlite3.connect('movies.db')
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data


def recommend_movies(user_id, num_recommendations=5):
    """Recommend movies based on user ratings."""
    ratings = fetch_data("SELECT * FROM ratings")
    movies = fetch_data("SELECT * FROM movies")

    user_ratings = ratings[ratings['user_id'] == user_id]
    rated_movie_ids = user_ratings['movie_id'].tolist()

    # Example recommendation logic: Recommend movies that the user hasn't rated yet
    unrated_movies = movies[~movies['movie_id'].isin(rated_movie_ids)]
    top_recommendations = unrated_movies.head(num_recommendations)

    return top_recommendations


if __name__ == "__main__":
    user_id = 1  # Example user_id
    recommendations = recommend_movies(user_id)
    print("Recommended Movies:")
    print(recommendations)
