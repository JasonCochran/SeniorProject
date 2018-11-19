from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import functions
from geoalchemy2.types import Geometry
import datetime
from app import db
from app.models import Recommendation, Prediction
import geojson
import random

# class Recommendation(db.Model):
#     _tablename_ = 'recommendation'
#     id = db.Column(db.Integer, primary_key = True)
#     recommendation = db.Column(db.String(132))
#     location = db.Column(Geometry('POINT'))

# Create how ever many dummy predictions we want
def createDummyRecommendations(num):
    for i in range(0,num):
        rec = Recommendation()
        rec.location = "POINT( " + str(round(random.uniform(-87.958428,-87.503532), 6)) + " " + str(round(random.uniform(41.640071,42.029866), 6)) + " )"
        rec.recommendation = "Create a grocery store here."
        db.session.add(rec)
    db.session.commit()
    print("Created " + str(num) + " dummy recommendations.")

createDummyRecommendations(5)
