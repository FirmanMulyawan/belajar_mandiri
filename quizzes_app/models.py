import datetime
from flask_sqlalchemy import SQLAlchemy
from app import db



class Kuis(db.Model):
    __tablename__ = 'quizzes'

    quiz_id = db.Column(db.Integer, primary_key = True)
    creator_id = db.Column(db.Integer())
    title = db.Column(db.String())
    quiz_category = db.Column(db.String())
    play_times = db.Column(db.Integer())
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    modified_at = db.Column(db.DateTime, default=datetime.datetime.now)
    deleted_at = db.Column(db.DateTime, default=datetime.datetime.now)
    
    def __init__(self, creator_id, title, quiz_category, play_times, created_at, modified_at, deleted_at):
        
        self.creator_id = creator_id
        self.title = title
        self.quiz_category = quiz_category
        self.play_times = play_times
        self.created_at = created_at
        self.modified_at = modified_at
        self.deleted_at = deleted_at

    def __repr__(self):
        return '<quizzes id{}>'.format(self.quiz_id)

    def serialize(self):
        return {
            'quiz_id': self.quiz_id,
            'creator_id': self.creator_id,
            'title': self.title,
            'quiz_category': self.quiz_category,
            'play_times': self.play_times,
            'created_at': self.created_at,
            'modified_at': self.modified_at,
            'deleted_at': self.deleted_at
        }

