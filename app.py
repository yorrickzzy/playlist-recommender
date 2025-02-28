from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

with open("playlist_rules.pkl", "rb") as f:
    rules = pickle.load(f)

@app.route("/")
def index():
    return render_template("index.html")  

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
