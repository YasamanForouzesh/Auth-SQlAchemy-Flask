# Import flask to app.y
# __name__ represent the current file
# We are saying that we want to have flask app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import *
import os
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="Heroku_Database_URL"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
def main():
    db.create_all()
if __name__ == "__main__":
    with app.app_context():
        main()