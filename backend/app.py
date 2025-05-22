from flask import Flask, request, jsonify
from flask_cors import CORS
from recommender.content_recommender import recommend
import requests
import os
from recommender.movie_list_loader import get_random_movies, search_movies


app = Flask(__name__)
CORS(app)

# TMDB API Key
TMDB_API_KEY = '3a98d330d97f726800c5d3954712bb21'


def get_poster(movie_title):
    url = f"https://api.themoviedb.org/3/search/movie"
    params = {'api_key': TMDB_API_KEY, 'query': movie_title}

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return None

    data = response.json()
    results = data.get('results')

    if not results:
        return None

    poster_path = results[0].get('poster_path')
    if poster_path:
        return f"https://image.tmdb.org/t/p/w500{poster_path}"

    return None

@app.route('/quick-suggestions', methods=['GET'])
def quick_suggestions():
    import json
    with open('static/quick_suggestions.json', 'r') as f:
        data = json.load(f)
    return jsonify({'suggestions': data})


@app.route('/suggest', methods=['GET'])
def suggest_movies():
    query = request.args.get('q', '')
    if query:
        titles = search_movies(query)
    else:
        titles = get_random_movies()
    
    result = []
    for title in titles:
        poster = get_poster(title)
        result.append({
            'title': title,
            'poster': poster
        })
    return jsonify({'suggestions': result})


# API endpoint for recommendations
@app.route('/recommend', methods=['POST'])
def recommend_movies():
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({'error': 'Missing "title" in request body'}), 400

    movie_title = data['title']
    recommendations = recommend(movie_title)

    result = []
    for rec in recommendations:
        poster_url = get_poster(rec)
        result.append({
            'title': rec,
            'poster': poster_url
        })


    return jsonify({'recommendations': result})


if __name__ == '__main__':
    app.run(debug=True)
