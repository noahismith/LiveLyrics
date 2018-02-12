from app import db
from datetime import datetime

# LiveLyrics User(username, password)
class User(db.Model):
	__tablename__ = 'Users'
	
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(255), unique=True, nullable=False)
	password = db.Column(db.String(255), unique=False, nullable=False)
	
	def __init__(self, username):
		self.username = username
		self.password = password

	def __repr__(self):
		return 'id: {}, username: {}'.format(self.id, self.username)
	
	# save(): adds User object to database
	def save(self):
		db.session.add(self)
		db.session.ommit()

	# delete(): deletes User object from database
	def delete(self):
        	db.session.delete(self)
        	db.session.commit()
	
	@staticmethod
    	def get_all():
        	return User.query.all()	

			
# Lyrics(songtitle, songlyrics, lyrictimestamps)
class Lyrics(db.Model):
	__tablename__ = 'Lyrics'
	
	id = db.Column(db.Integer, primary_key=True)
	songtitle = db.Column(db.String(255), unique=True, nullable=False)
	
	# songlyrics and lyrictimestamps are two arrays that hold the lyric and timestamp at equal index
	songlyrics = db.Column(db.ARRAY(db.String(255)))
	lyrictimestamps = db.Column(db.ARRAY(db.Integer))
	
	# the number of contributions that have been made to the lyrics of this song
	contributions = db.Column(db.Integer)
	
	def __init__(self, songtitle, songlyrics, lyrictimestamps):
		self.songtitle = songtitle
		self.songlyrics = songlyrics
		self.lyrictimestamps = lyrictimestamps
		
	def __repr__(self):
		return 'id: {}, songtitle: {}'.format(self.id, self.songtitle)
	
	# save(): adds Lyric object to database
	def save(self):
		db.session.add(self)
		db.session.commit()
	
	# delete(): deletes Lyric object from database
	def delete(self):
		db.session.delete(self)
		db.session.commit()
		
	@staticmethod
	def get_all():
		return Lyrics.query.all()
