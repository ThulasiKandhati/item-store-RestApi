import app import app
from db import db
@app.before_first_request
def create_tables():
	db.create_all()