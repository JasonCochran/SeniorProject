from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from werkzeug import secure_filename
from app import app, db, models, forms, logic
import os, sys

@app.route('/')
def index():
	# Get the list of all currently processing jobs
	# Also link to Spark, Hadoop, and MySQL GUI
	return render_template('home.html')

@app.route('/ingest/', methods=['GET','POST'])
def ingest():
#	form = forms.IngestForm()
	returnObject = {"form":forms.IngestForm(), "filename":None, "id":None, "error":None, "ingestResult":None}
	if returnObject["form"].validate_on_submit():
		returnObject["filename"] = secure_filename(returnObject["form"].submittedFile.data.filename)
		type = returnObject["form"].fileType.data
		try:
			returnObject["form"].submittedFile.data.save('../uploads/' + returnObject["filename"] )
			ingestFunc = getattr(logic, returnObject["form"].fileType.data )
			returnObject["ingestResult"] =  ingestFunc('../uploads/' + returnObject["filename"] )
		except:
			returnObject["filename"]=None
			returnObject["error"] = "Error occured while attempting to ingest the file."
			print("Unexpected error:" + sys.exc_info()[0] )
		returnObject["form"].submittedFile.data = ''
		returnObject["form"].fileType.data = ''
	return render_template('ingest.html', form=returnObject["form"], filename=returnObject["filename"], id=id, retObj=returnObject)

@app.route('/newProject/', methods=['GET','POST'] )
def newProject():
	form = forms.newProject()
	filename = None
	returnObject = {"form":forms.newProject(), "filename":None, "id":None, "error":None, "ingestResult":None}
	if form.validate_on_submit():
		print("test2")
		filename = secure_filename(form.submittedFile.data.filename)
#		try:
		returnObject["form"].submittedFile.data.save('../uploads/' + filename)
		returnVal = logic.metadata('../uploads/' + filename)
#		except:
		returnObject["error"] = "Error occured while attempting to ingest the file."
#		print("Unexpected error:" + sys.exc_info()[0] )
		returnObject["form"].submittedFile.data = ''
	return render_template('newProject.html', form=form, filename=filename)

@app.route('/view/', methods=['GET', 'POST'])
def view():
	form = forms.ViewForm()
	data = db.session.query(models.Project).join(models.ContactPerson).add_columns(models.ContactPerson.firstName, models.ContactPerson.lastName,
		models.ContactPerson.phone, models.ContactPerson.address, models.ContactPerson.email).all()
	return render_template('view.html', data=data, form=form)

@app.route('/project/<projectID>/')
def project(projectID):
	data = db.session.query(models.Project).join(models.ContactPerson).add_columns(models.ContactPerson.firstName,
		models.ContactPerson.lastName, models.ContactPerson.phone, models.ContactPerson.address,
		models.ContactPerson.email).filter(models.Project.id == projectID).first()
	studies = db.session.query(models.Study).filter(models.Study.projectID == data[0].id).all()
	files = db.session.query(models.File).filter(models.File.studyId == studies[0].id)
#	files = []
#	for study in studies:
#		files.append( db.session.query(models.File.filter(study.id == models.File.studyId) )
	return render_template('project.html', data=data, studies=studies, files=files)
