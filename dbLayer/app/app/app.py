from flask import Flask, render_template, jsonify
from werkzeug import secure_filename
from app import app, db, models
import os, sys, json

@app.route('/')
def index():
    return 'Pred Pol Database Data Curation script. Purely used for uploading data to PostGIS.'

@app.route('/jsonData/<file>', methods=['GET'])
def getJSON(file):
	file = 'test.json'
	static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
	file_path = os.path.join(static_file_dir, file)
	with open(file_path, 'r') as file_data:
		json_data = json.load(file_data)
	return jsonify(json_data)
