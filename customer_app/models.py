import datetime
from flask_sqlalchemy import SQLAlchemy
from app import db

# db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'customer'

    customer_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    email = db.Column(db.String())
    created_on = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<customer id{}>'.format(self.customer_id)

    def serialize(self):
        return {
            'customer_id': self.customer_id,
            'username': self.username,
            'password': self.password,
            'email': self.email
        }

