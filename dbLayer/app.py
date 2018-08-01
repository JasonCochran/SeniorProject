from flask import request, jsonify, abort
app = flask.Flask('dbAPILayer')

@app.route('/incidents/', methods=['POST','GET'])
def index():
        if request.method == "POST":
		response = jsonify( {} )
		response.status_code = 201
		return response

	else if request.method == "GET":
		results = []
		for objects in list:
			obj = {}
			results.append(obj)
		
		response = jsonify(results)
		response.status_code = 200
		return response

	return app
