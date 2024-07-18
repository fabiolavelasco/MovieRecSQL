# Movie Recommendation System

## Overview

This project is a movie recommendation system built using Python and SQLite. The system processes movie and rating data, and provides insights and recommendations based on user ratings.

## Features

- **Data Ingestion**: Load and clean movie and rating data from CSV files.
- **Database Management**: Store and manage data using SQLite.
- **Data Visualization**: Generate visualizations to display top-rated movies.
- **Recommendation Engine**: (Optional) Implement recommendation algorithms to suggest movies.



## Scripts

- `data_processing.py`: Handles data loading, cleaning, and inserting into the SQLite database.
- `database.py`: Manages SQLite database connection and schema creation.
- `visualization.py`: Generates and displays plots for movie ratings and recommendations.
- `recommendation.py`: Contains algorithms to recommend movies based on user preferences.

## Data

- **Movies Data**: `movies.csv` - Contains movie IDs, titles, and genres.
- **Ratings Data**: `ratings.csv` - Contains user IDs, movie IDs, ratings, and timestamps.
- **Users Data**: `u.user` - Contains user IDs, genders, ages, occupations, and zip codes.

## Example Output

The following command generates a horizontal bar chart of top-rated movies:

```python
import matplotlib.pyplot as plt

# Assuming top_movies is a DataFrame with columns 'title' and 'avg_rating'
top_movies.plot(kind='barh', x='title', y='avg_rating', legend=False)

plt.xlabel('Average Rating')
plt.ylabel('Movie Title')
plt.title('Top 10 Movies')
plt.show()

