from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import functions
from geoalchemy2.types import Geometry
import datetime
from app import db
from app.models import Recommendation, Prediction
import geojson
import random

# class RiskFactorMetadata(db.Model):
# 	_tablename_ = 'RiskFactorMetadata'
# 	id = db.Column(db.Integer, primary_key = True)
# 	fileName = db.Column(db.String(132))

# class RiskFactor(db.Model):
# 	_tablename_ = 'riskFactor'
# 	id = db.Column(db.Integer, primary_key = True)
# 	value = db.Column(db.Float)
# 	metadata = db.Column(db.Integer, db.ForeignKey(RiskFactorMetadata.ID))
# 	location = db.Column(Geometry('POINT'))

def createDummyRiskFactors(num):
	DT = datetime.datetime.now()
    countIndex = 0
    rfmeta = RiskFactorMetadata()
    rfmeta.fileName = "blargh.csv"
    db.session.add(rfmeta)
    db.session.flush()
    db.session.refresh(rfmeta)

    for i in range(0,num):
        riskFactor = RiskFactor()
        riskFactor.location = "POINT( " + str(round(random.uniform(-87.958428,-87.503532), 6)) + " " + str(round(random.uniform(41.640071,42.029866), 6)) + " )"
        riskFactor.value = round(random.uniform(0, 1), 4)
        riskFactor.metadata = rfmeta.id
        db.session.add(rec)
    db.session.commit()
    print("Created " + str(num) + " dummy risk factor points.")

createDummyRiskFactors(50)
