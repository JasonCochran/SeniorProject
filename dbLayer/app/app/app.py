from flask import Flask, render_template, jsonify
from werkzeug import secure_filename
from app import app, db, models, persist
import os, sys, json


@app.route('/')
def index():
    return 'Pred Pol Database Data Curation script. Purely used for uploading data to PostGIS.'


# Get persisted JSON data
@app.route('/jsonData/<file>', methods=['GET'])
def getJSON(file):
	file = 'test.json'
	static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
	file_path = os.path.join(static_file_dir, file)
	with open(file_path, 'r') as file_data:
		json_data = json.load(file_data)
	return jsonify(json_data)


# Call to create a persisted JSON file for specific prediction
@app.route('/persist/<run_info>', methods=['POST'])
def persistEndpoint(run_info):
	result = persist.persist(run_info)
	return result
