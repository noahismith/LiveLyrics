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

class Lyrics(db.Model):
	__tablename__ = 'Lyrics'
	
	id = db.Column(db.Integer, primary_key=True)
	songtitle = db.Column(db.String(255), unique=True, nullable=False)
	songlyrics = db.Column(db.ARRAY(db.String(255)))
	lyrictimestamps = db.Column(db.ARRAY(db.Integer))
	contributions = db.Column(db.Integer)
	
	def __init__(self, songtitle, songlyrics, lyrictimestamps):
		self.songtitle = songtitle
		self.songlyrics = songlyrics
		self.lyrictimestamps = lyrictimestamps
		
	def __repr__(self):
		return 'id: {}, songtitle: {}'.format(self.id, self.songtitle)
		
	def save(self):
		db.session.add(self)
		db.session.commit()
		
	def delete(self):
		db.session.delete(self)
		db.session.commit()
		
	@staticmethod
	def get_all():
		return Lyrics.query.all()
