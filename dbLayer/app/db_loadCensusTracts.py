from app import db
from app.models import CensusTracts

import csv

filename = '/crimeCSV/CensusTractsTIGER2010.csv'
count = 0
with open(filename, "r") as csvfile:
	datareader = csv.reader(csvfile)
	next(datareader)
	count = 0
	for row in datareader:
		try:
			tempCT = CensusTracts()
#			tempCT.ID = row[0]
			tempCT.stateID = row[0]
			tempCT.geom = row[1]
			tempCT.countyID = row[2]
			tempCT.tractCE =  row[3]
			tempCT.geoID = row[4].strip()
			tempCT.name =  row[5]
			tempCT.nameLSAD =  row[6]
			tempCT.commarea =  row[7]

			db.session.add(tempCT)
			count = count + 1
		except Exception as e:
			print(e)
			db.session.rollback()

db.session.commit()
print("Done: " + str(count))
