from app import db
from app.models import Incident
import csv

filename = 'Crimes_-_2001_to_present.csv'
count = 0
with open(filename, "r") as csvfile:
	datareader = csv.reader(csvfile)
#       yield next(datareader)
	next(datareader)
	count = 0
	attempt = 0
	for row in datareader:
		attempt = attempt + 1
		try:
			tempInc = Incident()
			tempInc.ID = row[0]
			tempInc.caseNumber = row[1]
        	        # Date is 2
			tempInc.block = row[3]
			tempInc.IUCR = row[4]
			tempInc.primaryType = row[5]
			tempInc.description = row[6]
			# Location desc is 7
			if 'false' in row[8]:
				tempInc.arrest = 0
			else:
				tempInc.arrest = 1
			if 'false' in row[9]:
				tempInc.domestic = 0
			else:
				tempInc.domestic = 1
			tempInc.beat = row[10]
			tempInc.district = row[11]
			tempInc.ward = row[12]
			tempInc.communityArea = row[13]
			tempInc.FBIcode = row[14]
			if str(row[15]).strip():
				tempInc.xCoord = row[15]
			else:
				tempInc.xCoord = 0
			if str(row[16]).strip():
				tempInc.yCoord = row[16]
			else:
				tempInc.yCoord = 0
			tempInc.year = row[17]
			tempInc.updatedOn = row[18]
			if str(row[19]).strip():
				tempInc.latitude = row[19]
			else:
				tempInc.latitude = 0
			if str(row[20]).strip():
				tempInc.longitude = row[20]
			else:
				tempInc.longitude = 0
			
			if str(row[21]).strip():
				tempInc.location = row[21]
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
