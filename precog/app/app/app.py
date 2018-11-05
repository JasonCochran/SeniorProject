from flask import Flask, render_template
from werkzeug import secure_filename
from app import app, db, models
import os, sys, requests

@app.route('/')
def index():
        return 'Pre-Crime Division - Pre Cog'

#@app.route('/run')
def persistRun(runID):
	# eventually this can be endpoint that calls precog algo and persists run
	# runID = precogRun()
	result = requests.get('http://dblayer:80/persist/' + str(runID) )
	# return ('', 204)