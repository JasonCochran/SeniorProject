from flask import Flask, render_template
from werkzeug import secure_filename
from app import app, db, models
import os, sys, requests

def createRecommendation():
	profiles = db.session.query(models.RecommendationProfile),all()
	for profile in profiles:
		# Loop through each profile and look for things that fit this profile...
		# We pull the dataFeeder attribute and look for a table (maybe have this data stored as files?)
		# Maybe also require that the file has a specific format or has certain headers?
		# We can then run stats for each box over chicago against our imported data
		# This will consist of checking how far each box is from the other data we pulled in
		# Maybe we should do some sort of 'density' statistics to check for how many
		#		attributes exist in a certain area
	return "success"
