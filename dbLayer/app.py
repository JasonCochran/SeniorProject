from flask import request, jsonify, abort
app = flask.Flask('dbAPILayer')

# Note: The get returns ALL incidents!
@app.route('/incidents/', methods=['POST','GET'])
def incidents():
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

@app.route('/incidents/', methods=['GET'])
def incidentSearch():
	return response

def streetParse(string):
	# Expect 4 digit number, zero out the x's
	# Then take remainder as actual street address
	return None
