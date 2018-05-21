import flask
app = flask.Flask('Demo Flask')

@app.route('/')
def index():
	return "Web GUI"
