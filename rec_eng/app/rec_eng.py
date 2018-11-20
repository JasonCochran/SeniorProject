from app import app, db, models
import os, sys, requests
from riskFactors import AbandonedBuildings, FoodDeserts, LackOfTransportation
import numpy as np

def createRecommendations():
	originLat = float(os.environ['LATORG'])
	originLong = float(os.environ['LONORG'])
	limitLat = float(os.environ['LATSTOP'])
	limitLong = float(os.environ['LONSTOP'])
	bbsize = float(os.environ['BBSIZE'])
	bbsize=0.007
	NSBoxes = ( originLat - limitLat ) / bbsize
	EWBoxes = ( originLong - limitLong ) / bbsize
	matrixDepth = 4 # number of risk factors we are calculating against plus 1 (crime itself)
	riskMatrix = np.zeros( shape=( NSBoxes, EWBoxes, matrixDepth) )

	for x in np.arange(0, np.absolute(NSBoxes)):
		for y in np.arange(0, np.absolute(EWBoxes)):
			# Fish net algorithm
			p1xo = originLat - (x*bbsize)
			p1yo = originLong + (y*bbsize)
			p2xo = originLat - (x*bbsize)  - bbsize
			p2yo = originLong + (y*bbsize)
			p3xo = originLat - (x*bbsize) - bbsize
			p3yo = originLong + (y*bbsize) + bbsize
			p4xo = originLat - (x*bbsize)
			p4yo = originLong + (y*bbsize) + bbsize
			box = "POLYGON((" + str(p1xo) + " " + str(p1yo) + ", " + str(p2xo) + " " + str(p2yo) + ", " + str(p3xo) + " " + str(p3yo) \
			        + ", " + str(p4xo) + " " + str(p4yo) + ", " + str(p1xo) + " " + str(p1yo) +  "))"
			centerLat = ((originLat - (x*bbsize)) + (originLat - (x*bbsize)  - bbsize))/ 2
			centerLon = ((originLong + (y*bbsize)) + (originLong + (y*bbsize) + bbsize))/ 2

			# Collect the crime data
			crimeCount = db.session.query(Incident).filter(Incident.location.contained(box)).count()
			riskMatrix(x, y, 0) = crimeCount

			# Run some statistics to determine what areas we could help the most...
			# Once we assign overall 'badness' score and find top 5...
			# We should determine what we can do to help these areas
			# Use the highest of the 3 risk scores to determine what a solution could be

