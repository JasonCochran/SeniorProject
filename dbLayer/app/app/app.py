from flask import Flask, render_template, jsonify
from werkzeug import secure_filename
from app import app, db, models, persist
import os, sys, json


@app.route('/')
def index():
    return 'Pred Pol Database Data Curation script. Purely used for uploading data to PostGIS.'


def getFile(file, path):
	file_path = os.path.join(path, file)
	with open(file_path, 'r') as file_data:
		json_data = json.load(file_data)
	response = jsonify(json_data)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return jsonResult


# Get persisted JSON data
@app.route('/jsonData/<file>', methods=['GET'])
def getJSON(file):
	file = 'test.json'
	static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
	file_path = os.path.join(static_file_dir, file)
	with open(file_path, 'r') as file_data:
		json_data = json.load(file_data)
	return jsonify(json_data)


# Get list of all available precog runs (with all associated metadata)
@app.route('/precogruns/', methods=['GET'])
def getPreCogRuns():
	static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
	file_path = os.path.join(static_file_dir, "precogruns.json")
	with open(file_path, 'r') as file_data:
		json_data = json.load(file_data)
	response = jsonify(json_data)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response


# Get specific set of predictions based on precog run ID
@app.route('/prediction/<ID>', methods=['GET'])
def getPredictions(ID):
	file = ID
	static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
	file_path = os.path.join(static_file_dir, file + ".geojson")
	with open(file_path, 'r') as file_data:
		json_data = json.load(file_data)
	response = jsonify(json_data)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response


# Call to create a persisted JSON file for specific prediction
@app.route('/persist/<run_info>', methods=['GET'])
def persistEndpoint(run_info):
	filename = run_info
	result = persist.persistRun(run_info, filename)
	return ('', 204)
