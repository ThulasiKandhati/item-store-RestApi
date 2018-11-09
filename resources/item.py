from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
import sqlite3

class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('price',type=float,required=True,help='This filed cannot be left blank!')
	parser.add_argument('store_id',type=int,required=True,help='Every item should be linked with store!')
	@jwt_required()
	def get(self, name):
		row = ItemModel.find_by_name(name)		
		if row:
			return row.json(),200 
		return {'Message':'Item not found'},404

	
	def post(self,name):		
		if ItemModel.find_by_name(name):
			return {'Message':"Message with name '{}' already exists ".format(name)}
		data = Item.parser.parse_args()	
		#data = request.get_json()-- doenot require as we are parsing.
		itemo = ItemModel(name,data['price'],data['store_id'])
		try:
			itemo.save_item()
		except:
			return {'Message':"An error occured during insert"},500
		return itemo.json(),201

	def delete(self,name):
		# ItemModel.delete_item(name)
		# return {'Message':'Item Deleted'}
		item = Item.find_by_name(name)
		if item:
			item.delete_item()
		return  {'Message':'Item deleted'}
	def put(self,name):
		data = Item.parser.parse_args()
		item = ItemModel.find_by_name(name)
		item = ItemModel.find_by_name(name)
		if item is None:
			item = ItemModel(name,data['price'],data['store_id'])
		else:
			item.price = data['price']
		item.save_item()
		return item.json()
		#itemo = ItemModel(name,data['price'])
		#data = request.get_json()
		# if item is None:
		# 	try:
		# 		itemo.insert_item()
		# 	except:
		# 		return {"Message":"An error Occured during update"}
		# else:
		# 	try:
		# 		itemo.update_item()
		# 	except:
		# 		return {"Message":"An error Occured during update"}			
		# return item.json()

class itemList(Resource):

	def get(self):
		return {"items":self.find_name()}
	@classmethod
	def find_name(cls):
		#return {"items":list(map(lambda x:x.json(),ItemModel.query.all()))}
		return {'items':[x.json() for x in ItemModel.query.all()]}
		# itm = []
		# connection = sqlite3.connect('data.db')
		# cursor = connection.cursor()
		# result = cursor.execute("SELECT * FROM items")
		# for row in result:
		# 	itm.append({'Item':row[1],'Price':row[2 ]})
		# connection.close()
		# return itm	