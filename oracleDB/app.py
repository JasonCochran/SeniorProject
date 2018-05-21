import flask
app = flask.Flask('Demo Flask')

@app.route('/example')
def example():
	return "This is an example"
