from flask_sqlalchemy import SQLAlchemy

# Tworzymy instancje db bez aplikacji
db = SQLAlchemy()


class Shots(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scene_id = db.Column(db.String(100), nullable=False)
    shot_id_name = db.Column(db.String(100), nullable=False)
    time_to_roll_the_shot = db.Column(db.Integer, nullable=False)
    camera_shot_type = db.Column(db.String(100), nullable=False)
    camera_movement = db.Column(db.String(100), nullable=False)
    camera_id = db.Column(db.String(100), nullable=False)
    shot_description = db.Column(db.String(100), nullable=False)
    lighting = db.Column(db.String(100), nullable=False)
    actors = db.Column(db.String(100), nullable=False)
    props =db.Column(db.String(100), nullable=False)
    xmlFilename = db.Column(db.String(100), nullable=False)
    videoCodec = db.Column(db.String(100), nullable=False)
    deviceModel = db.Column(db.String(100), nullable=False)
    lensModel = db.Column(db.String(100), nullable=False)
    frameCount = db.Column(db.String(100), nullable=False)
    captureFps = db.Column(db.String(100), nullable=False)
    pixel = db.Column(db.String(100), nullable=False)
    numOfVerticalLine = db.Column(db.String(100), nullable=False)
    aspectRatio = db.Column(db.String(100), nullable=False)
    audioChannels = db.Column(db.String(100), nullable=False)
    audioCodec = db.Column(db.String(100), nullable=False)

