# It means User is inheretende from db.Model
# Import flask to app.y
# __name__ represent the current file
# We are saying that we want to have flask app
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy()
class User(UserMixin,db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    bio = db.Column(db.String, nullable = True)
    github = db.Column(db.String, nullable = True)
    linkdin = db.Column(db.String, nullable = True)
    bag = db.Column(db.String, nullable=True)

    
class Video(db.Model):
    __tablename__ = "videos"
    id = db.Column(db.Integer, primary_key=True)
    URL = db.Column(db.String, nullable = False)
    videoname = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)

class Comments(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey("videos.id"),nullable=False)
    text = db.Column(db.String, nullable = False)
    code = db.Column(db.String, nullable = False)
    imgURL = db.Column(db.String, nullable = False)
    
class Reply(db.Model):
    __tablename__ = "replies"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey("comments.id"), nullable=False)
    text = db.Column(db.String, nullable = False)
    code = db.Column(db.String, nullable = False)
    imgURL = db.Column(db.String, nullable = False)

def main():
    db.create_all()
if __name__ == "__main__":
    with app.app_context():
        main()