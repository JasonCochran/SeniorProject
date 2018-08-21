from app import db
from app.models import Incident
import csv

filename = 'Crimes_-_2001_to_present.csv'
with open(filename, "r") as csvfile:
        datareader = csv.reader(csvfile)
#       yield next(datareader)
        next(datareader)
        count = 0
        for row in datareader:
                tempInc = Incident()
                tempInc.ID = row[0]
                tempInc.caseNumber = row[1]
                # Date is 2
                tempInc.block = row[3]
                tempInc.IUCR = row[4]
                tempInc.primaryType = row[5] 
                tempInc.description = row[6]
                # Location desc is 7
                tempInc.arrest = row[8]
                tempInc.domestic = row[9]
                tempInc.beat = row[10]
                tempInc.district = row[11]
                tempInc.ward = row[12]
                tempInc.communityArea = row[13] 
                tempInc.FBIcode = row[14]
                tempInc.xCoord = row[15]
                tempInc.yCoord = row[16]
                tempInc.year = row[17]
                tempInc.updatedOn = row[18]
                tempInc.latitude = row[19]
                tempInc.longitude = row[20]
                tempInc.location = row[21]

                db.session.add(tempInc)                 

                if count % 50000 == 0:
                        print(count)
			db.session.commit()
                count = count + 1

db.session.commit()
