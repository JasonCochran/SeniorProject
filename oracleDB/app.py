import flask
app = flask.Flask('Demo Flask')

@app.route('/')
def example():
	return "This is an example"
