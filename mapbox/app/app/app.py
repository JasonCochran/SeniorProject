from flask import Flask, render_template
from werkzeug import secure_filename
from app import app, db, models
import os, sys, requests

@app.route('/',methods=['GET','POST'])
def my_maps():
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
