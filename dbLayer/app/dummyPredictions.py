from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import functions
from geoalchemy2.types import Geometry
import datetime
from app import db
from app.models import PreCogRun, Prediction
import geojson
import random


# Create how ever many dummy predictions we want
def createDummyPredictions(num):
    DT = datetime.datetime.now()
    countIndex = 0
    run = PreCogRun()
    run.type = "JSON TEST DATA ONLY"
    run.precog = "dumb"
    run.datetime = DT
    db.session.add(run)
    db.session.flush()
    db.session.refresh(run)
    for i in range(0,num):
        pred = Prediction()
        pred.precogrun=run.ID
        pred.certainty = round(random.uniform(0,1), 2)
        pred.countIndex =  countIndex + 1
#       pred.type = 'general'
#       pred.precog = 'basic_ml'
        pred.datetime = datetime.datetime(2018, 1, 1)
        pred.location = "POINT( " + str(round(random.uniform(-87.958428,-87.503532), 6)) + " " + str(round(random.uniform(41.640071,42.029866), 6)) + " )"
        db.session.add(pred)
        countIndex = countIndex + 1
    db.session.commit()

createDummyPredictions(10)
