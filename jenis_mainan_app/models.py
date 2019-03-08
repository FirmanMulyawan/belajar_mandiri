import datetime
from flask_sqlalchemy import SQLAlchemy
from app import db

# db = SQLAlchemy()

class jenis_mainan(db.Model):
    __tablename__ = 'jenis_mainan'

    mainan_id = db.Column(db.Integer, primary_key = True)
    nama_mainan = db.Column(db.String())
    pengguna = db.Column(db.String())
    harga = db.Column(db.Integer())
    
    def __init__(self, nama_mainan, pengguna, harga):
        self.nama_mainan = nama_mainan
        self.pengguna = pengguna
        self.harga = harga

    def __repr__(self):
        return '<mainan id{}>'.format(self.mainan_id)

    def serialize(self):
        return {
            'mainan_id': self.mainan_id,
            'nama_mainan': self.nama_mainan,
            'pengguna': self.pengguna,
            'harga': self.harga
        }

