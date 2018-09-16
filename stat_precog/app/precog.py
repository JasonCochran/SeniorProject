from app import db
from app.models import Prediction, Incident
from flask_sqlalchemy import SQLAlchemy
import os
import numpy as np

# Write pre cog here
def getIncidents(numRows):
    data = db.session.query(Incident).limit(5)
    print(data[0].arrest)

def runStats(numRows):
	originLat = float(os.environ['LATORG'])
	originLong = float(os.environ['LONORG'])
	limitLat = float(os.environ['LATSTOP'])
	limitLong = float(os.environ['LONSTOP'])
	bbsize = float(os.environ['BBSIZE'])
	NSBoxes = ( originLat - limitLat ) / bbsize
	EWBoxes = ( originLong - limitLong ) / bbsize
	locations = {}

	for x in np.arange(0, np.absolute(NSBoxes)):
    		# X loop
		for y in np.arange(0, np.absolute(EWBoxes)):
        		# Y loop
			print(x)
			print(y)
			p1x = originLat - (x*bbsize)
			p1y = originLong + (y*bbsize)
			p2x = originLat - (x*bbsize)  - bbsize
			p2y = originLong + (y*bbsize)
			p3x = originLat - (x*bbsize) - bbsize
			p3y = originLong + (y*bbsize) + bbsize
			p4x = originLat - (x*bbsize)
			p4y = originLong + (y*bbsize) + bbsize
			# Create a selection box to get all crimes in a certain region
			box = "POLYGON((" + str(p1x) + " " + str(p1y) + ", " + str(p2x) + " " + str(p2y) + ", " + str(p3x) + " " + str(p3y) \
                		+ ", " + str(p4x) + " " + str(p4y) + ", " + str(p1x) + " " + str(p1y) +  "))"
			print(box)
			result = db.session.query(Incident).filter(Incident.location.contained(box)).count()

			# Record how many crimes occur in each box
			

	# Run stats over the array, most likely just find max for normalization heat map

#	for x in range(originLat, limitLat): # X loop
#		for y in range(originLong, limitLong): # Y loop
#			# Compare our boxes crime to all other boxes
#			# Compute stats and record them as actual prediction

runStats(10)
