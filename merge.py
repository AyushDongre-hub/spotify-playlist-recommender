import pandas as pd
import os
os.makedirs("data", exist_ok=True)

# Corrected file names
df1 = pd.read_csv("SpotifyAudioFeaturesNov2018.csv")
df2 = pd.read_csv("SpotifyAudioFeaturesApril2019.csv")

# Combine and drop duplicates
df = pd.concat([df1, df2], ignore_index=True).drop_duplicates(subset="track_id")

# Save merged version
df.to_csv("data/combined_spotify_features.csv", index=False)
