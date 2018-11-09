from db import db

class StoreModel(db.Model):
	__tablename__ = 'stores'
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(80))
	country = db.Column(db.String(80))
	items = db.relationship('ItemModel', lazy ='dynamic')

	def __init__(self,name,country):
		self.name = name
		self.country = country

	def json(self):
		return{'name':self.name,'country':self.country,'items':[item.json() for item in self.items.all()]}
		
	@classmethod
	def find_by_name(cls,name):
		return cls.query.filter_by(name = name).first()
			
	def save_store(self):
		db.session.add(self)
		db.session.commit()

