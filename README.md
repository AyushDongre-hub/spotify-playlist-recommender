<<<<<<< HEAD
# 🎧 Content-Based Music Recommender

An offline Python-based music recommendation engine built using Spotify's audio features dataset. It finds similar songs using cosine similarity on audio feature vectors like danceability, energy, tempo, etc.

## 📁 Dataset
Merged two real Spotify audio feature datasets from 2018 and 2019 (Kaggle):
- SpotifyAudioFeaturesNov2018.csv
- SpotifyAudioFeaturesApril2019.csv

## 🧠 How It Works
- Input: User types a song name
- Engine extracts the song’s audio feature vector
- Compares it to 130,000+ tracks using cosine similarity
- Returns top similar songs instantly

## 🚀 Run Locally

```bash
pip install -r requirements.txt
python app.py
=======
# spotify-playlist-recommender
>>>>>>> 3a982f79dc9a9923a60fd63c2f34677085615362
