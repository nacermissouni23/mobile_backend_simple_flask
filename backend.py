from flask import Flask, jsonify
from flask_cors import CORS
import json
import datetime
import os

app = Flask(__name__)
CORS(app)  # <-- this enables all origins to access the API

# --- ROUTE: Get All News ---
@app.route('/news.all.get')
def get_news_all_articles():
    try:
        with open('news_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- ROUTE: Get Categories ---
@app.route('/news.categories.get')
def get_news_categories():
    time_now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {
        'title': 'List of Categories',
        'time': time_now_str,
        'categories': [
            {'id': 1, 'name': 'Sports'},
            {'id': 2, 'name': 'Politics'},
            {'id': 3, 'name': 'Education'}
        ]
    }
    return jsonify(data)

# --- ROOT ROUTE ---
@app.route('/')
def index():
    return '✅ Flask API is running successfully on Leapcell!'

# --- MAIN ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
