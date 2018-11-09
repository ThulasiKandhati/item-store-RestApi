from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.store import StoreModel

class Store(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('country',type=str,required=True,help='This filed cannot be left blank!')
	
	@jwt_required()
	def put(self,name):
		data = Store.parser.parse_args()
		store = StoreModel.find_by_name(name)
		if store is None:
			store = StoreModel(name,data['country'])
		else:
			store.country = data['country']
		store.save_store()
		return store.json()

class StoreList(Resource):
	def get(self):
		return {"Stores":self.find_name()}
	@classmethod
	def find_name(cls):
		return {'stores':[x.json() for x in StoreModel.query.all()]}
		