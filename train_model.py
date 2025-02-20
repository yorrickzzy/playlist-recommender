from fpgrowth_py import fpgrowth
import pandas as pd
import pickle

# 加载数据集
df = pd.read_csv("/home/datasets/spotify/2023_spotify_ds1.csv")
df['track_name'] = df['track_name'].str.strip().str.lower()  # 移除空格 + 统一小写
df['track_name'] = df['track_name'].str.rstrip('.')
transactions = df.groupby("pid")["track_name"].apply(list).tolist()

# 运行 FPGrowth 频繁项集挖掘
freqItemSet, rules = fpgrowth(transactions, minSupRatio=0.1, minConf=0.5)

# 保存模型
with open("playlist_rules.pkl", "wb") as f:
    pickle.dump(rules, f)
print("模型已保存！")
