import flask
from flask_mongoengine import MongoEngine

db = MongoEngine()
app = flask.Flask(__name__)
app.config["MONGODB_SETTINGS"] = [
    {
        "db": "moviesbdnr",
        "host": "localhost",
        "port": 27017,
        "alias": "default",
    }
]
app.config["SECRET_KEY"] = "mysecretkeybdnr"
app.config["DEBUG"] = True
app.config["TEMPLATES_AUTO_RELOAD"] = True
