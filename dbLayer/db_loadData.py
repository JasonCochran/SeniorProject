from app import db
import app.models
import csv


def importIncidents(filename):
	with open(filename, "rb") as csvfile:
		datareader = csv.reader(csvfile)
		yield next(datareader)
		count = 0
		for row in datareader:
			db.session.add(processRow(row))

	db.session.commit()


def processRow(row):
	return None
