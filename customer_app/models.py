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
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())
    movies = db.relationship('Movie_rented', backref='customer', lazy=True)

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
            'email': self.email,
            'created_on':self.created_on,
            'movies': [{'movie':item.movies_rented} for item in self.movies]
        }

class Movie_rented(db.Model):
    __tablename__ = 'movie_rented'

    rent_id = db.Column(db.Integer, primary_key = True)
    cstr_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    movies_rented = db.Column(db.String())

    def __init__(self, movies_rented):
        self.movies_rented = movies_rented
    
    def __repr__(self):
        return '<rent id{}>'.format(self.rent_id)

