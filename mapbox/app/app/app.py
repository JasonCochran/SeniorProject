from flask import Flask, render_template
from werkzeug import secure_filename
from app import app, db, models
import os, sys, requests

@app.route('/',methods=['GET','POST'])
def my_maps():
	return render_template('index.html')

@app.route('/about', methods=['GET','POST'])
def about():
	return render_template('about.html')

@app.route('/urgent', methods=['GET','POST'])
def urgent():
	return render_template('urgent.html')

@app.route('/admin', methods=['GET','POST'])
def admin():
		# Call other backend services for heartbeat request
	status = {"dbLayer":None,"precog":None,"nn_precog":None,"rec_eng":None,"stat_precog":None}
	status["dbLayer"]     = "1" if (requests.get('http://dblayer:81/heartbeat').status_code == 204) else "0"
	status["precog"]      = "1" if (requests.get('http://dblayer:82/heartbeat').status_code == 204) else "0"
	status["nn_precog"]   = "1" if (requests.get('http://dblayer:87/heartbeat').status_code == 204) else "0"
	status["rec_eng"]     = "1" if (requests.get('http://dblayer:86/heartbeat').status_code == 204) else "0"
	status["stat_precog"] = "1" if (requests.get('http://dblayer:84/heartbeat').status_code == 204) else "0"
	return render_template('admin.html', status)
