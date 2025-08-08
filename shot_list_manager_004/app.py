import os
from flask import Flask
from routes import my_blueprint
from routes import my_blueprint_002

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shot_list.db'

from models import db
db.init_app(app)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(my_blueprint)
app.register_blueprint(my_blueprint_002)

with app.app_context():
    db.create_all() # Tworzenie tabel w bazie danych jesli nie istnieja

if __name__ == "__main__":
    app.run(debug=True)