from flask import Flask, render_template
from werkzeug import secure_filename
from app import app, db, models
import os, sys, requests

@app.route('/',methods=['GET','POST'])
def my_maps():
	# Can we request from dblayer:81 ?? It should be in the same Docker network
	response = requests.get('172.18.0.7:81/jsonData/test.json')
	#print(response.json)
	return render_template('index.html')

@app.route('/recommendations', methods=['GET','POST'])
def recommendation():
	return render_template('recommendations.html')

@app.route('/urgent', methods=['GET','POST'])
def urgent():
	return render_template('urgent.html')

@app.route('/admin', methods=['GET','POST'])
def admin():
	return render_template('admin.html')