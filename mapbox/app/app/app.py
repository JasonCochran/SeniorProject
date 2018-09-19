from flask import Flask, render_template
from werkzeug import secure_filename
from app import app, db, models
import os, sys

@app.route('/',methods=['GET','POST'])
def my_maps():

 #  mapbox_access_token = 'pk.eyJ1IjoibWV0cmljb24iLCJhIjoiY2l3eTQxMWl3MDBmYTJ6cWg3YmZtdjdsMSJ9.2vDbTw3ysscpy3YWkHo6aA'
  mapbox_access_token = ''
  return render_template('index.html', mapbox_access_token=mapbox_access_token)
