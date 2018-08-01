from flask_sqlalchemy import SQLAlchemy
from app import db

class ContactPerson(db.Model):
        _tablename_ = 'contactperson'
        id = db.Column(db.Integer, primary_key = True)
        firstName = db.Column(db.String(255))
        lastName = db.Column(db.String(255))
        phone = db.Column(db.String(255))
        address = db.Column(db.String(255))
        email = db.Column(db.String(255))
