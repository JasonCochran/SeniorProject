from app import db
from app.models import Prediction, Incident
from flask_sqlalchemy import SQLAlchemy
import os
import datetime
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sqlalchemy import and_

def runStats():
        curDT = datetime.datetime.now() 
        years = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
        originLat = float(os.environ['LATORG'])
        originLong = float(os.environ['LONORG'])
        limitLat = float(os.environ['LATSTOP'])
        limitLong = float(os.environ['LONSTOP'])
        bbsize = float(os.environ['BBSIZE'])
        bbsize=0.007
        NSBoxes = ( originLat - limitLat ) / bbsize
        EWBoxes = ( originLong - limitLong ) / bbsize
        crimeCounts = []
        boxes = []
        X, y = make_regression(n_features=3, n_informative=3,random_state=42, shuffle=True)
        NSBoxes = ( originLat - limitLat ) / bbsize
        EWBoxes = ( originLong - limitLong ) / bbsize
        crimeCounts = []
        boxes = []
        for x in np.arange(0, np.absolute(NSBoxes)):
                # X loop
                for y in np.arange(0, np.absolute(EWBoxes)):
                    for year in years:
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

                        result = db.session.query(Incident).filter(and_(Incident.location.contained(box)),Incident.year==year).count()
#                        if result==0:
#                            continue
                        x = ((originLat - (x*bbsize)) + (originLat - (x*bbsize)  - bbsize))/ 2
                        y = ((originLong + (y*bbsize)) + (originLong + (y*bbsize) + bbsize))/ 2
                        boxes.append([x,y,year])
                        crimeCounts.append(result)
                        if(result>0):
                            print("number of crimes is ")
                            print(result)
                        
                        



        # Run stats over the array, most likely just find max for normalization heat map
        #maxCrimes = max(crimeCounts)
        regr = RandomForestRegressor(max_depth=3, random_state=42)
        features = np.array(boxes[:int(len(boxes)/2)])
        output = np.array(crimeCounts[:int(len(crimeCounts)/2)])
        testFeatures = np.array(boxes[int(len(boxes)/2):])
        testOutput = np.array(crimeCounts[int(len(crimeCounts)/2):])
        regr.fit(features, output)
        print(regr.score(testFeatures,testOutput))
        countIndex = 0
    
        for x in np.arange(0, np.absolute(NSBoxes)):
                # X loop
                for y in np.arange(0, np.absolute(EWBoxes)):
                    for year in years:
                        # Y loop
                        # Create predictions for each grid location
                        # Create central point
                        x = ((originLat - (x*bbsize)) + (originLat - (x*bbsize)  - bbsize))/ 2
                        y = ((originLong + (y*bbsize)) + (originLong + (y*bbsize) + bbsize))/ 2
                        pred = Prediction()
                        predic = regr.predict([[x,y,year]])[0]
                        #print(predic)
                        pred.certainty = predic
                        pred.countIndex =  countIndex + 1
                        pred.type = 'general'
                        pred.precog = 'basic_ml'
                        pred.datetime = curDT
                        pred.location = "POINT( " + str(x) + " " + str(y) + " )"
                        db.session.add(pred)
#                       print("POINT( " + str(x) + " " + str(y) + " )")
#                       print(crimeCounts[countIndex] / maxCrimes)
                        countIndex = countIndex + 1
        db.session.commit()

runStats()
print("Stats pre cog finished running")
