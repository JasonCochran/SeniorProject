from flask_sqlalchemy import SQLAlchemy
from app import db

class Incident(db.Model):
	_tablename_ = 'incident'
	ID = db.Column(db.Integer, primary_key = True)
	caseNumber = db.Column(db.String(15))
	block = db.Column(db.String(132))
	IUCR = db.Column(db.Integer(10))
	primaryType = db.Column(
	description = db.Column(db.String(64))
	locationDescription = db.Column(db.String(132))
	arrest = db.Column(db.Boolean)
	domestic = db.Column(db.Boolean)
	beat = db.Column(db.Integer(10))
	district = db.Column(db.Integer(10))
	ward = db.Column(db.Integer(10))
	communityArea = db.Column(db.Integer(10))
	FBIcode = db.Column(db.Integer(10))
	xCoord = db.Column(db.Integer(32))
	yCoord = db.Column(db.Integer(32))
	year = db.Column(db.Integer(4))
	updatedOn = db.Column(db.String(32))
	latitude = db.Column(db.Integer(64))
	longitude = db.Column(db.Integer(64))
	location = db.Column(db.String(132))
