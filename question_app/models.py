import datetime
from flask_sqlalchemy import SQLAlchemy
from app import db



class ClassQuestion(db.Model):
    __tablename__ = 'questions'

    id_questions = db.Column(db.Integer, primary_key = True)
    quiz_id = db.Column(db.Integer())
    question = db.Column(db.String())
    number = db.Column(db.Integer())
    answer = db.Column(db.String())
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    modified_at = db.Column(db.DateTime, default=datetime.datetime.now)
    deleted_at = db.Column(db.DateTime, default=datetime.datetime.now)
    
    def __init__(self, quiz_id, question, number, answer, created_at, modified_at, deleted_at):
        
        self.quiz_id = quiz_id
        self.question = question
        self.number = number
        self.answer = answer
        self.created_at = created_at
        self.modified_at = modified_at
        self.deleted_at = deleted_at

    def __repr__(self):
        return '<questions id{}>'.format(self.quiz_id)

    def serialize(self):
        return {
            'id_questions': self.id_questions,
            'quiz_id': self.quiz_id,
            'question': self.question,
            'number': self.number,
            'answer': self.answer,
            'created_at': self.created_at,
            'modified_at': self.modified_at,
            'deleted_at': self.deleted_at
        }

