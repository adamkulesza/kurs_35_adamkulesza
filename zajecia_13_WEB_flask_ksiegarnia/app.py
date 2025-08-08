from flask import Flask

from routes import ksiegarnia_blueprint

app = Flask(__name__)
app.register_blueprint(ksiegarnia_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
