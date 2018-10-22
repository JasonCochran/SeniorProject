# SeniorProject
Greg and Jason's senior project repo. Contains Useful links for research and tech information.

## Installation instructions.
* Note: These are for production setup
* Clone the git directory: git clone <repo url>
* Run 'docker-compose up --build'
* Download the Chicago crime data in CSV format and put it in the 'crimeCSV' folder
* Download https://openmaptiles.com/downloads/tileset/osm/north-america/us/illinois/chicago/ and put it in the data folder
* Run crimecleaning.py in the root directory
* Run db_create.py and db_load.py in the dblayer container
* Do work (if you delete the postGIS container you have to re-create and re-load the data)

## Ideas for development order
* 1) Build the database -> PostGIS
* 2) Setup docker deployment system to automate setup and testing
* 3) Create the front end GUI to view basic things from the database
* 4) Create prediction algorithm (PreCog)
* 5) Create caching layer for GUI, emphasize speed
* 6) Create additional data aggregators and more prediction abilities
* 7) Graduate

## Purpose for each directory
* dbLayer        - holds scripts to create and upload data to a PostGIS database using SQLAlchemy + GeoAlchemy
* webGUI         - Act as the GUI for the predictive policing software
* precog         - Basic ML precog
* stats_precog   - Basic precog using simple statistics
* cpdScraper     - Scrape the Chicago Police Department crime database daily for new information
* twittersuicide - Program to scrape Twitter for tweets that indicate possible suicide

## Interesting predictive policing links
* Chicago crime data 2001 - present (updated daily... Maybe we can pull daily?) https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present-Dashboard/5cd6-ry5g
* Chicago strategic subjects list (anonymized but still useful possibly) https://data.cityofchicago.org/Public-Safety/Strategic-Subject-List-Dashboard/wgnt-sjgb
* Chicago suicide study (need hard statistical data combined with Twitter maybe) https://link.springer.com/article/10.1007/BF00584047

## Algorithms links

## Frameworks / tech stack links
* Really useful REST API link: https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way
* A useful CI/CD deployment software that might be nice to use. We could probably deploy with very little work. https://concourse-ci.org/
* Open source graphing library (not sure about performance for large projects with this) https://plot.ly/
* GIS Spatial Addition to PostGRES http://www.postgis.net/
* Probably the best way to deploy Python apps to a web platform. We can use these for testing as well. https://www.docker.com/
* Useful for container orchestration possibly. Using simple Docker containers might just be easier though. https://kubernetes.io/
* Flask - static website generation using Python and markdown language. Probbaly the best bet for creating the site itself. We could also use this to create the microservices possibly... http://flask.pocoo.org/
* Python Linters: https://jeffknupp.com/blog/2016/12/09/how-python-linters-will-save-your-large-python-project/

## Useful research links
* Massive amounts of Twitter data https://archive.org/search.php?query=collection%3Atwitterstream&sort=-publicdate&page=2
* Filtering Tweets by location (suicide) https://developer.twitter.com/en/docs/tutorials/filtering-tweets-by-location
* Microservice design books https://www.icbf.gov.co/sites/default/files/microservices_designing_deploying.pdf
* https://www.nginx.com/wp-content/uploads/2015/01/Building_Microservices_Nginx.pdf
* http://nealford.com/downloads/Building_Microservice_Architectures_Neal_Ford.pdf
* Async microservice discussion http://eventuate.io/whyeventdriven.html
* http://geopandas.org/gallery/plotting_with_geoplot.html

## Greg's plan
Chicago police data->postGIS->algorithm->web interface
divide chicago into block sizes that reflect the precision of the crime location data
map available crime data onto those geoblocks
map additional factor data onto those geoblocks
calculate information gain/entropy with regards to each attribute associated with all blocks containing a targeted crime
sort attributes by information gain
branch on the highest entropy attribute-record entropy and attribute
repeat until the tree is finished, either all attributes used or all remaining attributes have low information gain
run

## Useful commands
* Login to db (must be logged into PostGIS container): psql -h 127.0.0.1 -d predpol -U ppuser
* Login into container: docker exec -it [container name] bash
