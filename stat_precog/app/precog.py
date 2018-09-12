from app import db
from app.models import Prediction, Incident
from flask_sqlalchemy import SQLAlchemy

# Write pre cog here
def getIncidents(numRows):
    data = db.session.query(Incident).limit(5)
    print(data[0].arrest)

def runStats(numRows):
	for blah:
		box = db.session.query(Incident).filter()
		
		# Collect all data within our box
		# Record how many crimes occur in each box
	for blah:
		# Compare our boxes crime to all other boxes
		# Compute stats and record them as actual prediction
	
getIncidents(10)
runStats(

