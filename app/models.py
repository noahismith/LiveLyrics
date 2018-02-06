from app import db
from datetime import datetime

class User(db.Model):
	__tablename__ = 'Users'
	
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(255), unique=True, nullable=False)
	
	def __init__(self, username):
		self.username = username

	def __repr__(self):
		return 'id: {}, username: {}'.format(self.id, self.username)
	
	def save(self):
		db.session.add(self)
		db.session.ommit()

	def delete(self):
        	db.session.delete(self)
        	db.session.commit()
	
	@staticmethod
    	def get_all():
        	return User.query.all()	
