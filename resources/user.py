from flask_restful import Resource,reqparse
from models.user import UserModel


class UserRegister(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('username',type=str,required=True,help='Username filed cannot be left blank!')
	parser.add_argument('password',type=str,required=True,help='Password filed cannot be left blank!')
		
	def post(self):
		data = UserRegister.parser.parse_args()
		user = UserModel(**data)
		#try:
		user.save_todb()
		#except:
		#	return{'Message':'Unable to create User.'},500
		
		return{'Message':'User created sucessfully'},201	
			