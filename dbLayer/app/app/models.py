from flask_sqlalchemy import SQLAlchemy
from geoalchemy2.types import Geometry
from app import db

class Incident(db.Model):
	_tablename_ = 'incident'
	ID = db.Column(db.Integer, primary_key = True)
	caseNumber = db.Column(db.String(15))
	date = db.Column(db.DateTime)
	block = db.Column(db.String(132))
	IUCR = db.Column(db.String(10))
	primaryType = db.Column(db.String(132))
	description = db.Column(db.String(64))
	locationDescription = db.Column(db.String(132))
	arrest = db.Column(db.Boolean)
	domestic = db.Column(db.Boolean)
	beat = db.Column(db.Float, server_default='0')
	district = db.Column(db.Float, server_default='0')
	ward = db.Column(db.Float, server_default='0')
	communityArea = db.Column(db.Float)
	FBIcode = db.Column(db.String(20))
	xCoord = db.Column(db.Float, default = '')
	yCoord = db.Column(db.Float, default = '')
	year = db.Column(db.Integer)
	updatedOn = db.Column(db.String(32))
	latitude = db.Column(db.Float, default = '')
	longitude = db.Column(db.Float, default = '')
	location = db.Column(Geometry('POINT'))

class Beat(db.Model):
	_tablename_ = 'beat'
	ID = db.Column(db.Integer, primary_key = True)
	beat = db.Column(db.Integer)
	beat_num = db.Column(db.Integer)
	district = db.Column(db.Integer)
	geom = db.Column(Geometry('MULTIPOLYGON'))

class PreCogRun(db.Model):
	_tablename_ = 'precogrun'
	ID = db.Column(db.Integer, primary_key = True)
	type = db.Column(db.String(132))
	precog = db.Column(db.String(16))
	datetime = db.Column(db.DateTime)

class Prediction(db.Model):
	_tablename_ = 'prediction'
	ID = db.Column(db.Integer, primary_key = True)
	precogrun = db.Column(db.Integer, db.ForeignKey(PreCogRun.ID))
	certainty = db.Column(db.Float)
	location = db.Column(Geometry('POINT'))
	datetime = db.Column(db.DateTime)	

class Recommendation(db.Model):
	_tablename_ = 'recommendation'
	ID = db.Column(db.Integer, primary_key = True)
	type = db.Column(db.String)
	urgency = db.Column(db.Float)
	location = db.Column(Geometry('POINT'))

class PoliceStation(db.Model):
	_tablename_ = 'policestation'
	district = db.Column(db.String, primary_key = True)
	districtName = db.Column(db.String(255))
	address = db.Column(db.String(255))
	city = db.Column(db.String(132))
	state = db.Column(db.String(64))
	zip = db.Column(db.Integer)
	website = db.Column(db.String(132))
	phone = db.Column(db.String(32))
	fax = db.Column(db.String(32))
	tty = db.Column(db.String(32))
	location = db.Column(Geometry('POINT'))

# class SexOffenders(db.Model):

# class Districts(db.Model):

class CensusTracts(db.Model):
	_tablename_ = "censustract"
	ID = db.Column(db.Integer, primary_key = True)
	stateID = db.Column(db.Integer)
	geom = db.Column(Geometry('MULTIPOLYGON'))
	countyID = db.Column(db.Integer)
	tractCE = db.Column(db.String(32))
	geoID = db.Column(db.String(32))
	name = db.Column(db.String(32))
	nameLSAD = db.Column(db.String(32))
	commarea = db.Column(db.Integer)
