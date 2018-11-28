#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 00:08:13 2018

@author: paul
"""

from app import db
from app.models import Prediction, Incident, PreCogRun
from flask_sqlalchemy import SQLAlchemy
import os
import datetime
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sqlalchemy import and_
from sqlalchemy import *
from sqlalchemy import func
import time
from sklearn import *
import sklearn
from sklearn.externals import joblib
from tempfile import TemporaryFile
from sklearn.model_selection import RandomizedSearchCV
import math
crimeCounts = []
boxes = []
testcrimeCounts = []
testboxes = []
def commitToDB(rf):
        curDT = datetime.datetime.now() 
#        tryears = [2001,2002,2003,2004,2005,2006]
#        tyears = [2007,2008,2009,2010]
        tryears = [2001, 2002]
        tyears = [2003, 2004]
        years = tryears + tyears
        months = range(1,13)
        originLat = float(os.environ['LATORG'])
        originLong = float(os.environ['LONORG'])
        limitLat = float(os.environ['LATSTOP'])
        limitLong = float(os.environ['LONSTOP'])
        bbsize = float(os.environ['BBSIZE'])
        bbsize=0.007
        NSBoxes = ( originLat - limitLat ) / bbsize
        EWBoxes = ( originLong - limitLong ) / bbsize
        DT = datetime.datetime.now() 
        countIndex = 0
        run = PreCogRun()
        run.type = "thefts by box-months using random forest"
        run.precog = "MRFT"
        run.datetime = DT
        db.session.add(run)
        db.session.flush()
        db.session.refresh(run)
        for x in np.arange(0, np.absolute(NSBoxes)):
                # X loop
                for y in np.arange(0, np.absolute(EWBoxes)):
                    for year in years:
                        for month in months:
                            centerLat = ((originLat - (x*bbsize)) + (originLat - (x*bbsize)  - bbsize))/ 2
                            centerLon = ((originLong + (y*bbsize)) + (originLong + (y*bbsize) + bbsize))/ 2
                            pred = Prediction()
                            predic = rf.predict([[centerLon,centerLat,year,month]])[0]
                            pred.precogrun=run.ID
                            pred.certainty = predic
                            pred.countIndex =  countIndex + 1
    #                            pred.type = 'general'
    #                            pred.precog = 'basic_ml'
                            pred.datetime = datetime.datetime(year, month, 1)
                            pred.location = "POINT( " + str(centerLon) + " " + str(centerLat) + " )"
                            db.session.add(pred)
                            countIndex = countIndex + 1
        db.session.commit()
def runStats():
        curDT = datetime.datetime.now() 
#        tryears = [2001,2002,2003,2004,2005,2006]
#        tyears = [2007,2008,2009,2010]
        tryears = [2001, 2002]
        tyears = [2003, 2004]
        years = tryears + tyears
        months = range(1,13)
        originLat = float(os.environ['LATORG'])
        originLong = float(os.environ['LONORG'])
        limitLat = float(os.environ['LATSTOP'])
        limitLong = float(os.environ['LONSTOP'])
        bbsize = float(os.environ['BBSIZE'])
        bbsize=0.007
        NSBoxes = ( originLat - limitLat ) / bbsize
        EWBoxes = ( originLong - limitLong ) / bbsize
        global crimeCounts
        global boxes
        crimeCounts = []
        boxes = []
        #X, y = make_regression(n_features=4, n_informative=4,random_state=42, shuffle=False)
        NSBoxes = ( originLat - limitLat ) / bbsize
        EWBoxes = ( originLong - limitLong ) / bbsize
        totalCrimes=0
        j =0
        maxCrimes = 0
        start = time.time()
        for x in np.arange(0, np.absolute(NSBoxes)):
            # X loop
            for y in np.arange(0, np.absolute(EWBoxes)):
                j+=1
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
                boxResult = db.session.query(Incident).filter(Incident.location.contained(box))
                if(boxResult.count()==0):
                    continue    
                print("box number ", j)
                print("max count ", maxCrimes)
                print("total crimes ",totalCrimes)                
                for year in tryears:
                    yearResult = boxResult.filter(Incident.year==year)
                    for month in months:
                        monthResult = yearResult.filter(and_(func.extract('month',Incident.date)==month),Incident.FBIcode=="06")
                        count = monthResult.count()
                        boxes.append([centerLon,centerLat,year,month])
                        crimeCounts.append(count)
                        if count>maxCrimes:
                            maxCrimes=count
                        totalCrimes= totalCrimes + count
        global testcrimeCounts
        global testboxes
        for x in np.arange(0, np.absolute(NSBoxes)):
            for y in np.arange(0, np.absolute(EWBoxes)):
                j+=1
                p1x = originLat - (x*bbsize)
                p1y = originLong + (y*bbsize)
                p2x = originLat - (x*bbsize)  - bbsize
                p2y = originLong + (y*bbsize)
                p3x = originLat - (x*bbsize) - bbsize
                p3y = originLong + (y*bbsize) + bbsize
                p4x = originLat - (x*bbsize)
                p4y = originLong + (y*bbsize) + bbsize
                box = "POLYGON((" + str(p1x) + " " + str(p1y) + ", " + str(p2x) + " " + str(p2y) + ", " + str(p3x) + " " + str(p3y) \
                        + ", " + str(p4x) + " " + str(p4y) + ", " + str(p1x) + " " + str(p1y) +  "))"
                centerLat = ((originLat - (x*bbsize)) + (originLat - (x*bbsize)  - bbsize))/ 2
                centerLon = ((originLong + (y*bbsize)) + (originLong + (y*bbsize) + bbsize))/ 2  
                print("box number ", j)
                print("max count ", maxCrimes)
                print("total crimes ",totalCrimes)     
                boxResult = db.session.query(Incident).filter(Incident.location.contained(box))
                if(boxResult.count()==0):
                    continue       
                for year in tyears:
                    yearResult = boxResult.filter(Incident.year==year)
                    for month in months:
                        monthResult = yearResult.filter(and_(func.extract('month',Incident.date)==month),Incident.FBIcode=="06")
                        count = monthResult.count()
                        testboxes.append([centerLon,centerLat,year,month])
                        testcrimeCounts.append(count)
                        if count>maxCrimes:
                            maxCrimes=count
                        totalCrimes= totalCrimes + count          
        rf = RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=80,
           max_features='auto', max_leaf_nodes=None,
           min_impurity_decrease=0.0, min_impurity_split=None,
           min_samples_leaf=1, min_samples_split=2,
           min_weight_fraction_leaf=0.0, n_estimators=5, n_jobs=None,
           oob_score=False, random_state=0, verbose=0, warm_start=False)
        rf=RandomForestRegressor()
        rf.fit(boxes,crimeCounts)
        n_estimators = [int(x) for x in np.linspace(start = 10, stop = 2000, num = 10)]
        max_features = ['auto', 'sqrt']
        max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
        max_depth.append(None)
        min_samples_split = [2, 10]
        min_samples_leaf = [1, 2, 4, 10]
        bootstrap = [True, False]
#        random_grid = {'n_estimators': n_estimators,
#                       'max_features': max_features,
#                       'max_depth': max_depth,
#                       'min_samples_split': min_samples_split,
#                       'min_samples_leaf': min_samples_leaf,
#                       'bootstrap': bootstrap}
#        rf_random = RandomizedSearchCV(estimator = rf, scoring="r2", param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1,refit=False)
#        rf_random.fit(boxes, crimeCounts)
        
        #print("best parameters are ",rf_random.best_estimator_)
        features = boxes
        output = crimeCounts
        testFeatures = testboxes
        testOutput = testcrimeCounts
        rf = RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=30,
           max_features='sqrt', max_leaf_nodes=None,
           min_impurity_decrease=0.0, min_impurity_split=None,
           min_samples_leaf=2, min_samples_split=5,
           min_weight_fraction_leaf=0.0, n_estimators=400, n_jobs=None,
           oob_score=False, random_state=0, verbose=0, warm_start=False)
        rf.fit(features, output)
        predic = rf.predict(testFeatures)
        joblib.dump(rf, 'precogMonths.joblib') 
#        variance = sklearn.metrics.explained_variance_score(testOutput, predic, sample_weight=None, multioutput='uniform_average')
        r2 = sklearn.metrics.r2_score(testOutput, predic, sample_weight=None, multioutput="uniform_average")
        print("score ", rf.score(testFeatures,testOutput))
        print("r2 ", r2)
        commitToDB(rf)

runStats()


    
