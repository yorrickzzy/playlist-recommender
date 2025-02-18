'''
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# 加载推荐规则
with open("/app/models/recommendation_rules.pkl", "rb") as f:
    rules = pickle.load(f)

@app.route("/api/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    user_songs = {song.strip().lower().rstrip('.') for song in data["songs"]}  # 用户提供的歌曲列表

    # 查找符合条件的推荐
    recommendations = []
    for rule in rules:
        if user_songs.issuperset(rule[0]):  # 如果用户的歌曲符合规则
            recommendations.extend(rule[1])  # 添加推荐的歌曲

    return jsonify({
        "songs": list(set(recommendations)),  
        "version": "1.0",  
        "model_date": "2025-02-17"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=52011)
'''
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# 加载推荐模型
with open("playlist_rules.pkl", "rb") as f:
    rules = pickle.load(f)

@app.route("/api/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    user_songs = {song.strip().lower().rstrip('.') for song in data["songs"]}

    recommendations = set()
    for rule in rules:
        antecedent, consequent, confidence = rule
        if antecedent.issubset(user_songs):
            recommendations.update(consequent)

    return jsonify({
        "songs": list(recommendations),
        "version": "1.0",
        "model_date": "2025-02-17"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=52011)
