from db import db


class UserModel(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(80))
	password = db.Column(db.String(80))

	def __init__(self,username,password):
		self.username = username
		self.password = password

	def save_todb(self):
		db.session.add(self)
		db.session.commit()
		# if UserModel.find_by_username(data['username']):
		# 	return{'Message':"Username not avialble'{}'".format(data['username'])}			
		# connection = sqlite3.connect('data.db')
		# cursor = connection.cursor()
		# query = "INSERT INTO users VALUES(NULL,?,?)"
		# cursor.execute(query,(data['username'],data['password']))
		# connection.commit()
		# connection.close()

	@classmethod	
	def find_by_username(cls,username):
		return cls.query.filter_by(username = username).first()
		# con = sqlite3.connect('data.db')
		# cursor =con.cursor()
		# query = "SELECT * FROM users WHERE username=?"
		# result = cursor.execute(query,(username,))
		# row= result.fetchone()
		# if row is not None:
		# 	user = cls(*row)
		# else:
		# 	user = None
		# con.close()
		# return user

	@classmethod
	def find_by_userid(cls,_id):
		return cls.query.filter_by(id = _id).first()
		# con = sqlite3.connect('data.db')
		# cursor =con.cursor()
		# query = "SELECT * FROM users WHERE userid=?"
		# result = cursor.execute(query,(_id,))
		# row= result.fetchone()
		# if row is not None:
		# 	user = cls(*row)
		# else:
		# 	user = None
		# con.close()
		# return user
