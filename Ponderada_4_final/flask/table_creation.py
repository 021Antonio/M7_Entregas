from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()



class Account(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(100), nullable=False)
        password = db.Column(db.String(300), nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(100), nullable=False)
    post_text = db.Column(db.String(400), nullable=False)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    impluse = db.Column(db.Integer, nullable=False)
    pressurehight = db.Column(db.Integer, nullable=False)
    pressurelow = db.Column(db.Integer, nullable=False)
    glucose = db.Column(db.Integer, nullable=False)
    kcm = db.Column(db.Integer, nullable=False)
    troponin = db.Column(db.Integer, nullable=False)
    

def create_table(app):

    with app.app_context():
        db.create_all()

def main():
    create_table()

if __name__ == "__main__":
    main()