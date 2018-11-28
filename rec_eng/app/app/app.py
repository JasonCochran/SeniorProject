from flask import Flask, render_template
from werkzeug import secure_filename
from app import app, db, models
import os, sys

@app.route('/')
def index():
        return 'Pre-Crime Division - Pre Cog'	

@app.route('/heartbeat', methods=['GET'])
def heartbeat():
	return ('', 204)