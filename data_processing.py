import pandas as pd
import sqlite3


def load_data():
    # Load data from CSV files
    users = pd.read_csv('u.user', sep='|', names=['user_id', 'age', 'gender', 'occupation', 'zip_code'])
    movies = pd.read_csv('movies.csv', sep=',', names=['movie_id', 'title', 'genres'])
    ratings = pd.read_csv('ratings.csv', sep=',', names=['user_id', 'movie_id', 'rating', 'timestamp'])

    # Clean data
    users = users.drop_duplicates(subset=['user_id'])
    movies = movies.drop_duplicates(subset=['movie_id'])
    ratings = ratings.drop_duplicates(subset=['user_id', 'movie_id'])
    users = users.astype({'user_id': 'int32', 'gender': 'str', 'age': 'int32', 'occupation': 'str', 'zip_code': 'str'})
    movies = movies.astype({'movie_id': 'int32', 'title': 'str', 'genres': 'str'})
    ratings = ratings.astype({'user_id': 'int32', 'movie_id': 'int32', 'rating': 'float32', 'timestamp': 'int64'})

    return users, movies, ratings


def insert_data(users, movies, ratings):
    # Connect to SQLite database
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        gender TEXT,
        age INTEGER,
        occupation TEXT,
        zip_code TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        movie_id INTEGER PRIMARY KEY,
        title TEXT,
        genres TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ratings (
        user_id INTEGER,
        movie_id INTEGER,
        rating FLOAT,
        timestamp INTEGER,
        PRIMARY KEY (user_id, movie_id),
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
    )
    ''')

    # Insert data into tables
    users.to_sql('users', conn, if_exists='append', index=False)
    movies.to_sql('movies', conn, if_exists='append', index=False)
    ratings.to_sql('ratings', conn, if_exists='append', index=False)

    # Commit and close
    conn.commit()
    conn.close()


if __name__ == "__main__":
    users, movies, ratings = load_data()
    insert_data(users, movies, ratings)
