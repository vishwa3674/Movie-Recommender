import React, { useState } from 'react';
import axios from 'axios';
import './Recommender.css';

const Recommender = () => {
  const [movie, setMovie] = useState('');
  const [recommendations, setRecommendations] = useState([]);
  const [suggestions, setSuggestions] = useState([]);
  const [showSuggestions, setShowSuggestions] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleInputFocus = async () => {
    try {
      const res = await axios.get('http://127.0.0.1:5000/quick-suggestions');
      setSuggestions(res.data.suggestions);
      setShowSuggestions(true);
    } catch (err) {
      console.error('Error fetching suggestions:', err);
    }
  };

  const handleInputChange = async (e) => {
    const val = e.target.value;
    setMovie(val);
    setShowSuggestions(true);

    try {
      const res = await axios.get(`http://127.0.0.1:5000/suggest?q=${val}`);
      setSuggestions(res.data.suggestions);
    } catch (err) {
      console.error('Error fetching filtered suggestions:', err);
    }
  };


  const handleSuggestionClick = (title) => {
    setMovie(title);
    setShowSuggestions(false);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setRecommendations([]);

    try {
      const res = await axios.post('http://127.0.0.1:5000/recommend', {
        title: movie
      });
      setRecommendations(res.data.recommendations);
      setShowSuggestions(false);
    } catch (err) {
      console.error('Error getting recommendations:', err);
    }

    setLoading(false);

  };

  return (
    <div className="recommender-wrapper">
      <h1 className="title">Movie Recommender 🎬</h1>
      <form className="search-form" onSubmit={handleSubmit}>
        <div className="input-group">
          <input
            type="text"
            placeholder="Enter a movie name"
            value={movie}
            onFocus={handleInputFocus}
            onChange={handleInputChange}
            required
          />
          <button type="submit">Get Recommendations</button>
          {showSuggestions && suggestions.length > 0 && (
            <div className="suggestion-box">
              {suggestions.map((m, index) => (
                <div
                  className="suggestion-item"
                  key={index}
                  onClick={() => handleSuggestionClick(m.title)}
                >
                  {m.poster && <img src={m.poster} alt={m.title} />}
                  <div className="text-info">
                    <span>{m.title}</span>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </form>

      <div className="results">
        {loading ? (
          <div className="loading-message">Please wait, loading recommendations...</div>
        ) : (
          recommendations.map((rec, index) => (
            <a 
              key={index}
              href={`https://www.google.com/search?q=${encodeURIComponent(rec.title + ' movie')}`}
              target="_blank"
              rel="noopener noreferrer"
              className="movie-card-link"
            > 
            <div className="movie-card">
              <img src={rec.poster} alt={rec.title} />
              <h3>{rec.title}</h3>
            </div>
            </a>
          ))
        )}
      </div>
    </div>

  );
};

export default Recommender;
