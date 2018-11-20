from geoalchemy2 import func
from geoalchemy2.types import Geometry
from app import db
from app.models import PreCogRun, Prediction, Recommendation
import geojson, os, codecs
import pandas as pd
from collections import namedtuple
import datetime
import json


# Feed in PreCogRuns table query result
def geojsonConvert_PreCogRuns(queryResult):
	collection = {}
	print(queryResult.size)
	for data in queryResult.itertuples(index=True, name='Pandas'):
		collection[data.ID] = data.type
	d = {"name":"PreCogRuns",
	     "children":[{'type':value,"id":key} for key,value in collection.items()]}
	json_string = json.dumps(d)
	print(json_string)
	return json_string


# Feed in PreCogRuns table query result
def geojsonConvert_Recommendation(queryResult):
	collection = []
	print(queryResult.size)
	for data in queryResult.itertuples(index=True, name='Pandas'):
		point = geojson.Point(( data[1] , data[2] ))
		feature = geojson.Feature(geometry= point , properties={"rec": data.recommendation} )
		collection.append(feature)
	dump = geojson.dumps(geojson.FeatureCollection(collection))
	# print(dump)
	return dump


# Feed in a Predictions table query result
def geojsonConvert_Predictions(queryResult):
	collection = []
	print(queryResult.size)
	for data in queryResult.itertuples(index=True, name='Pandas'):
		point = geojson.Point(( data[1] , data[2] ))
		date = str(data.datetime.month) + "-" + str(data.datetime.year)
		feature = geojson.Feature(geometry= point , properties={"certainty": data.certainty, "date": date} )
		collection.append(feature)
	dump = geojson.dumps(geojson.FeatureCollection(collection))
	# print(dump)
	return dump


# Persist a specific precog run from db
def persistRun(runID, filename):
	result = db.session.query( func.ST_X(Prediction.location), func.ST_Y(Prediction.location), Prediction.certainty, Prediction.datetime ).filter(Prediction.precogrun == runID)
	data = pd.read_sql( result.statement , result.session.bind)
	geojson = geojsonConvert_Predictions(data)
	file_path = os.path.join("/app/app/static", filename + ".geojson")
	with codecs.open( file_path, 'w', encoding="utf8") as fo:
		fo.write(geojson)


# Persist all available precog runs from the db
def persist_all():
	return "success"


# def persist_riskFactors():
# 	result = db.session.query(PreCogRun)
# 	data = pd.read_sql( result.statement , result.session.bind)
# 	json = geojsonConvert_PreCogRuns(data)
# 	file_path = os.path.join("/app/app/static", "riskFactors.json")
# 	with codecs.open( file_path, 'w', encoding="utf8") as fo:
# 		fo.write(json)


def persist_recommendations():
	result = db.session.query( func.ST_X(Recommendation.location), func.ST_Y(Recommendation.location), Recommendation.recommendation, Recommendation.id)
	data = pd.read_sql( result.statement , result.session.bind)
	json = geojsonConvert_Recommendation(data)
	file_path = os.path.join("/app/app/static", "recommendations.geojson")
	with codecs.open( file_path, 'w', encoding="utf8") as fo:
		fo.write(json)


def persist_available_runs():
	result = db.session.query(PreCogRun)
	data = pd.read_sql( result.statement , result.session.bind)
	json = geojsonConvert_PreCogRuns(data)
	file_path = os.path.join("/app/app/static", "precogruns.json")
	with codecs.open( file_path, 'w', encoding="utf8") as fo:
		fo.write(json)