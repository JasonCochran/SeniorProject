from app import db
from app.models import Prediction, Incident
from flask_sqlalchemy import SQLAlchemy
import os
import datetime
import numpy as np

def runStats():
	curDT = datetime.datetime.now() 
	originLat = float(os.environ['LATORG'])
	originLong = float(os.environ['LONORG'])
	limitLat = float(os.environ['LATSTOP'])
	limitLong = float(os.environ['LONSTOP'])
	bbsize = float(os.environ['BBSIZE'])
	NSBoxes = ( originLat - limitLat ) / bbsize
	EWBoxes = ( originLong - limitLong ) / bbsize
	crimeCounts = []

	for x in np.arange(0, np.absolute(NSBoxes)):
    		# X loop
		for y in np.arange(0, np.absolute(EWBoxes)):
        		# Y loop
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
			result = db.session.query(Incident).filter(Incident.location.contained(box)).count()
			crimeCounts.append(result)

	# Run stats over the array, most likely just find max for normalization heat map
	maxCrimes = max(crimeCounts)

	countIndex = 0
	for x in np.arange(0, np.absolute(NSBoxes)):
		# X loop
		for y in np.arange(0, np.absolute(EWBoxes)):
			# Y loop
			# Create predictions for each grid location
			# Create central point
			x = ((originLat - (x*bbsize)) + (originLat - (x*bbsize)  - bbsize))/ 2
			y = ((originLong + (y*bbsize)) + (originLong + (y*bbsize) + bbsize))/ 2
			pred = Prediction()
			pred.certainty = crimeCounts[countIndex] / maxCrimes
			pred.countIndex =  countIndex + 1
			pred.type = 'general'
			pred.precog = 'basic_stats'
			pred.datetime = curDT
			pred.location = "POINT( " + str(x) + " " + str(y) + " )"
			db.session.add(pred)
#			print("POINT( " + str(x) + " " + str(y) + " )")
#			print(crimeCounts[countIndex] / maxCrimes)
			countIndex = countIndex + 1
	db.session.commit()

runStats()
print("Stats pre cog finished running")
