import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from routes import my_blueprint
from routes import my_blueprint_002

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(my_blueprint)
app.register_blueprint(my_blueprint_002)


if __name__ == "__main__":
    app.run(debug=True)