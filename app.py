import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load data
df = pd.read_csv("data/combined_spotify_features.csv")

# Audio feature columns
audio_cols = [
    'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
    'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo'
]

df.dropna(subset=audio_cols + ['track_name', 'artist_name'], inplace=True)
df['track_name_lower'] = df['track_name'].str.lower()

def recommend(song_name, top_n=5):
    song_name = song_name.lower()
    matches = df[df['track_name_lower'].str.contains(song_name)]

    if matches.empty:
        print("❌ Song not found in database.")
        return

    idx = matches.index[0]
    target_vec = df.loc[idx, audio_cols].values.reshape(1, -1)

    feature_matrix = df[audio_cols].values
    similarities = cosine_similarity(target_vec, feature_matrix)[0]

    # Get top similar songs
    top_indices = similarities.argsort()[::-1][1:top_n+1]

    print(f"\n🎧 Top {top_n} similar songs to '{df.loc[idx, 'track_name']}' by {df.loc[idx, 'artist_name']}:\n")
    for i in top_indices:
        print(f"{df.loc[i, 'track_name']} by {df.loc[i, 'artist_name']} (score: {similarities[i]:.2f})")

if __name__ == "__main__":
    song = input("Enter a song name: ")
    recommend(song)
