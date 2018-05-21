import flask.views

class Endpoint(flask.views.MethodView):
	def post(self):
		flask.abort(405)
	
	def get(self, id):
		flask.abort(405)

	def put(self, id):
		flask.abort(405)

	def delete(self, id):
		flask.abort(405)

	@classmethod
	def register(class_, app, base = '', default_id = None):
		view = class_.as_view(class_.__name__)

		app.add_url_rule('{}/{}'.format(base
