from app import db
from app.models import Prediction, Incident
from flask_sqlalchemy import SQLAlchemy
# Write pre cog here
def getIncidents(numRows):
    data = db.session.query(Incident).limit(5)
    print(data[0].arrest)
getIncidents(10)
    