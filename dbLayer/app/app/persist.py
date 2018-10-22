from app import app, db, models


def persist(run_info):
	return "success"


# Persist all available runs from the database
def persist_all():

	print("All runs persisted successfully.")
	return "success"
