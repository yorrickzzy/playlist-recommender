from fpgrowth_py import fpgrowth
import pandas as pd
import pickle

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(BASE_DIR, "../dataset/dataset/dataset_v2.csv")

if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"Dataset file not found: {dataset_path}")

df = pd.read_csv(dataset_path)

#df = pd.read_csv("/home/datasets/spotify/2023_spotify_ds2.csv")
df['track_name'] = df['track_name'].str.strip().str.lower()  
df['track_name'] = df['track_name'].str.rstrip('.')
transactions = df.groupby("pid")["track_name"].apply(list).tolist()

freqItemSet, rules = fpgrowth(transactions, minSupRatio=0.1, minConf=0.5)

with open("playlist_rules.pkl", "wb") as f:
    pickle.dump(rules, f)
print("Model Saved！")
