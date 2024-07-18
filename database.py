import sqlite3


def connect_db(db_name='movies.db'):
    """Create a connection to the SQLite database."""
    conn = sqlite3.connect(db_name)
    return conn


def create_tables(conn):
    """Create tables in the database."""
    cursor = conn.cursor()

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


def close_connection(conn):
    """Close the database connection."""
    conn.close()
