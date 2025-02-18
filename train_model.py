'''
import pandas as pd

# 读取数据集
df = pd.read_csv('/app/data/2023_spotify_ds1.csv')
#df = pd.read_csv('/home/datasets/spotify/2023_spotify_ds1.csv')
#df = pd.read_csv('/data/2023_spotify_ds1.csv')

# 只取 playlist_id 和 track_name
df = df[['pid', 'track_name']]
df['track_name'] = df['track_name'].str.strip().str.lower()  # 移除空格 + 统一小写
df['track_name'] = df['track_name'].str.rstrip('.')  # 移除末尾点号


# 将相同 playlist_id 的歌曲组合成列表
playlists = df.groupby('pid')['track_name'].apply(list).tolist()

# 输出示例
print(playlists[:3])  # 预览前3个播放列表

from fpgrowth_py import fpgrowth

# 设定最小支持度（support）和置信度（confidence）阈值
min_support = 0.1  # 至少 1% 播放列表包含该组合
min_confidence = 0.5  # 规则的可信度至少为 50%

# 生成频繁项集和关联规则
freqItemSet, rules = fpgrowth(playlists, minSupRatio=min_support, minConf=min_confidence)

# 输出示例
print("发现的规则:")
for rule in rules[:5]:  # 只显示前5条规则
    print(f"If {rule[0]} → Then {rule[1]}, Confidence: {rule[2]:.2f}")

import pickle

# 保存规则到文件
with open("/app/models/recommendation_rules.pkl", "wb") as f:
    pickle.dump(rules, f)

print("推荐规则已保存至 recommendation_rules.pkl")

# 重新加载模型
with open("recommendation_rules.pkl", "rb") as f:
    loaded_rules = pickle.load(f)

print(f"成功加载 {len(loaded_rules)} 条推荐规则！")
'''
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
