from app import db
from app.models import Prediction, Incident
from flask_sqlalchemy import SQLAlchemy

# Write pre cog here
def getIncidents(numRows):
    data = db.session.query(Incident).limit(5)
    print(data[0].arrest)

def runStats(numRows):
	originLat = os.environ['LATORG']
	originLong = os.environ['LONORG']
	limitLat = os.environ['LATSTOP']
	limitLong = os.environ['LONSTOP']

	locations = 

	for x in range(originLat, limitLat): # X loop
		for y in range(originLong, limitLong): # Y loop
			# Create a selection box to get all crimes in a certain region
			box = "POLYGON((" + p1x + " " + p1y + ", " + p2x + " " + p2y + ", " + p3x + " " + p3y + ", "     /
				+ p4x + " " + p4y + "))"
			print(box)
			result = db.session.query(Incident).filter(Incident.geom.contains(box)).count()

			# Record how many crimes occur in each box
			

	# Run stats over the array

	for x in range(originLat, limitLat): # X loop
		for y in range(originLong, limitLong): # Y loop
			# Compare our boxes crime to all other boxes
			# Compute stats and record them as actual prediction

runStats(10)
