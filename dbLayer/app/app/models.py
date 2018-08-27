from flask_sqlalchemy import SQLAlchemy
from app import db

class Incident(db.Model):
	_tablename_ = 'incident'
	ID = db.Column(db.Integer, primary_key = True)
	caseNumber = db.Column(db.String(15))
	block = db.Column(db.String(132))
	IUCR = db.Column(db.Integer)
	primaryType = db.Column(db.String(132))
	description = db.Column(db.String(64))
	locationDescription = db.Column(db.String(132))
	arrest = db.Column(db.Boolean)
	domestic = db.Column(db.Boolean)
	beat = db.Column(db.Integer)
	district = db.Column(db.Integer)
	ward = db.Column(db.Integer)
	communityArea = db.Column(db.Integer)
	FBIcode = db.Column(db.Integer)
	xCoord = db.Column(db.Float, default = '')
	yCoord = db.Column(db.Float, default = '')
	year = db.Column(db.Integer)
	updatedOn = db.Column(db.String(32))
	latitude = db.Column(db.Float, default = '')
	longitude = db.Column(db.Float, default = '')
	location = db.Column(db.String(132), default = '')
