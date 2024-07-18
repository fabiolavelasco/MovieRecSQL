import pandas as pd
import matplotlib.pyplot as plt
import sqlite3


def fetch_data(query):
    """Fetch data from the SQLite database."""
    conn = sqlite3.connect('movies.db')
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data


def plot_top_movies():
    """Generate and display a plot of top movies."""
    query = "SELECT title, AVG(rating) as avg_rating FROM movies JOIN ratings ON movies.movie_id = ratings.movie_id GROUP BY title ORDER BY avg_rating DESC LIMIT 10"
    top_movies = fetch_data(query)

    top_movies.plot(kind='barh', x='title', y='avg_rating', legend=False)
    plt.xlabel('Average Rating')
    plt.ylabel('Movie Title')
    plt.title('Top 10 Movies')
    plt.show()


if __name__ == "__main__":
    plot_top_movies()
