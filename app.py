from flask import Flask, render_template, send_from_directory
import json
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / 'data'
STATIC_DIR = BASE_DIR / 'static'

SONGS_FILE = DATA_DIR / 'songs.json'
PLAYLISTS_FILE = DATA_DIR / 'playlists.json'

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    songs = read_json(SONGS_FILE)[:10]
    playlists = read_json(PLAYLISTS_FILE)[:3]
    return render_template('index.html', songs=songs, playlists=playlists)

@app.route('/top10')
def top10():
    songs = read_json(SONGS_FILE)[:10]
    return render_template('top10.html', songs=songs)

@app.route('/pages')
def pages():
    playlists = read_json(PLAYLISTS_FILE)
    return render_template('pages.html', playlists=playlists)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(STATIC_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)