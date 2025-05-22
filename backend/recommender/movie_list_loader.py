import pandas as pd
import random

# Load the dataset once
movies = pd.read_csv('data/movies_metadata.csv', low_memory=False)
movies = movies[['title']].dropna().drop_duplicates()
movies = movies[movies['title'].apply(lambda x: isinstance(x, str) and len(x) > 0)]

def get_random_movies(count=6):
    return movies.sample(n=count)['title'].tolist()

def search_movies(query, count=6):
    filtered = movies[movies['title'].str.lower().str.contains(query.lower())]
    return filtered['title'].head(count).tolist()
