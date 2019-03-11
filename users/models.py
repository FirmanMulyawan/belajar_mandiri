import datetime
from flask_sqlalchemy import SQLAlchemy
from app import db

# db = SQLAlchemy()

class pengguna(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    fullname = db.Column(db.String())
    email = db.Column(db.String())    
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    modified_at = db.Column(db.DateTime, default=datetime.datetime.now)
    deleted_at = db.Column(db.DateTime, default=datetime.datetime.now)
    iniQuiz = db.relationship('Quizzesnya', backref='users', lazy=True)


    def __init__(self, username, password, fullname, email, created_at, modified_at, deleted_at):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email
        self.created_at = created_at
        self.modified_at = modified_at
        self.deleted_at = deleted_at

    def __repr__(self):
        return '<user id{}>'.format(self.user_id)

    def serialize(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'password': self.password,
            'fullname': self.fullname,
            'email': self.email,
            'created_at': self.created_at,
            'modified_at': self.modified_at,
            'deleted_at': self.deleted_at,
            'Quiz yang telah dibuat': [{'title':item.title} for item in self.iniQuiz]

        }

class Quizzesnya(db.Model):
    __tablename__ = 'quizzes'

    quiz_id = db.Column(db.Integer, primary_key = True)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    title = db.Column(db.String())
    quiz_category = db.Column(db.String())

    def __init__(self, quiz_category):
        self.quiz_category = quiz_category
    
    def __repr__(self):
        return '<quiz id{}>'.format(self.quiz_id)
