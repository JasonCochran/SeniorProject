from geoalchemy2 import func
from geoalchemy2.types import Geometry
from app import db
from app.models import PreCogRun, Prediction
import geojson, os, codecs
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


# Persist a specific precog run from db
def persistRun(runID, filename):
	result = db.session.query( func.ST_X(Prediction.location), func.ST_Y(Prediction.location), Prediction.certainty ).filter(Prediction.precogrun == runID)
	data = pd.read_sql( result.statement , result.session.bind)
	geojson = geojsonConvert(data)
	file_path = os.path.join("/app/app/static", filename + ".geojson")
	with codecs.open( file_path, 'w', encoding="utf8") as fo:
		fo.write(geojson)


# Persist all available precog runs from the db
def persist_all():
	return "success"

persistRun("6", "6")
