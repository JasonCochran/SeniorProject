from geoalchemy2 import func
from geoalchemy2.types import Geometry
from app import db
from shapely.wkb import loads
from app.models import PreCogRun, Prediction
import geojson
import pandas as pd


# Feed in a Predictions table query result
def geojsonConvert(queryResult):
	collection = []
	print(queryResult.size)
	for data in queryResult.itertuples(index=True, name='Pandas'):
		point = geojson.Point(( data[1] , data[2] ))
		feature = geojson.Feature(geometry= point , properties={"certainty": data.certainty} )
		collection.append(feature)
	dump = geojson.dumps(geojson.FeatureCollection(collection))
	print(dump)
	return dump


def persist(run_info):
	result = db.session.query( func.ST_X(Prediction.location), func.ST_Y(Prediction.location), Prediction.certainty )
	data = pd.read_sql( result.statement , result.session.bind)
	geojsonConvert(data)
	return "success"


# Persist all available runs from the database
def persist_all():
	return "success"


persist("blah")
