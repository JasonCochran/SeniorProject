from app import db
from app.models import Incident
import csv

filename = '/crimeCSV/PoliceBeatDec2012.csv'
count = 0
with open(filename, "r") as csvfile:
	datareader = csv.reader(csvfile)
	next(datareader)
	count = 0
	attempt = 0
	for row in datareader:
		attempt = attempt + 1
		try:
			tempInc = Incident()
			
			if str(row[20]).strip():
				tempInc.longitude = row[20]
			else:
				tempInc.longitude = 0
			
			if str(row[21]).strip():
				tempInc.location = "POINT(" +  row[19] + " " + row[20] + ")"
			else:
				tempInc.location = 0
			db.session.add(tempInc)
			db.session.commit()
			count = count + 1
			
		except Exception as e:
			print(e)
			db.session.rollback()
		if count % 50000 == 0:
			print(count)
		#	db.session.commit()
	#	count = count + 1

print("Done: " + count)
