import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Load and Clean dataset
movies = pd.read_csv('../data/movies_metadata.csv', low_memory=False)
movies = movies[['title', 'overview']]
movies.dropna(subset=['overview'], inplace=True)
movies.reset_index(drop=True, inplace=True)

#TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['overview'])

#Cosine Similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

#Index Mapping
indices = pd.Series(movies.index, index=movies['title'].str.lower())

#Recommendation Function
def recommend (movie_title, num_recommendations=5):
    movie_title = movie_title.lower()
    idx = indices.get(movie_title)

    if idx is None:
        return[]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]

    movie_indices = [i[0] for i in sim_scores]

    return movies['title'].iloc[movie_indices].tolist()
