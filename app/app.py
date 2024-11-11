from flask import Flask, render_template, send_from_directory, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, static_folder='static', media_folder='media')
app.config.from_object('config.Config')

# Initialize the database
db = SQLAlchemy(app)

# Serve static files
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(os.path.join(app.config['STATIC_FOLDER']), filename)

# Serve media files
@app.route('/media/<path:filename>')
def media_files(filename):
    return send_from_directory(os.path.join(app.config['MEDIA_FOLDER']), filename)

# Sample route
@app.route('/')
def index():
    return jsonify(message="Welcome to the Andromeda app!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
