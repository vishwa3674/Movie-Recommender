# 🎬 Movie Recommender System

An interactive movie recommender web application built with **React** (frontend) and **Flask** (backend). It suggests movies based on a given title and displays relevant posters using the TMDB API.

---

## 🚀 Features

- 🔍 Suggests 4–5 similar movies based on user input.
- 🎥 Displays movie posters using the TMDB API.
- ✨ Dynamic suggestions as the user types.
- 💡 Random movie suggestions on input focus.
- 🌐 Clickable cards that open a Google search in a new tab.

---


## 📁 Project Structure

```
Movie-Recommender/
├── backend/
│   ├── app.py
│   ├── recommender/
│   │   ├── content_recommender.py
│   │   └── movie_list_loader.py
│   └── data/
│       └── movies_metadata.csv
├── frontend/
│   └── src/
│       ├── components/
│       │   └── Recommender.js
│       ├── App.js
│       ├── index.js
│       └── Recommender.css
├── public/
│   └── index.html
└── README.md
```

---

## ⚙️ Setup Instructions

### 🔧 Backend (Flask)

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. *(Optional)* Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate     # On Windows
   source venv/bin/activate    # On macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask server:
   ```bash
   python app.py
   ```

   ✅ The backend API will run at: `http://127.0.0.1:5000`

---

### 🌐 Frontend (React)

5. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

6. Install React dependencies:
   ```bash
   npm install
   ```

7. Start the React app:
   ```bash
   npm start
   ```

   ✅ The frontend will launch at: `http://localhost:3000`

---

## 📦 APIs & Datasets

- [TMDB API](https://www.themoviedb.org/documentation/api) for fetching movie posters.
- `movies_metadata.csv` from [Kaggle's Movie Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset).

---


## 🙌 Acknowledgements

- Built with ❤️ by Vishwa Athukorala
