from app import db
import re


class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    spotify_id = db.Column(db.String(255), unique=True, nullable=False)
    birthdate = db.Column(db.DateTime, nullable=True)
    email = db.Column(db.String(255), unique=True)
    spotify_refresh_token = db.Column(db.String(255))
    num_of_contributions = db.Column(db.Integer, default=0)

    def __init__(self, username, spotify_id, birthdate, email, spotify_refresh_token):
        self.username = username
        self.spotify_id = spotify_id
        self.birthdate = birthdate
        self.email = email
        self.spotify_refresh_token = spotify_refresh_token
        self.num_of_contributions = -1

    def __repr__(self):
        return 'id: {}, username: {}, spotify_id: {}, birthdate: {}, email: {}' \
            .format(self.id, self.username, self.spotify_id, self.birthdate, self.email, self.num_of_contributions)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def toJSON(self):
        user = {
            "username": self.username,
            "spotify_id": self.spotify_id,
            "birthdate": self.birthdate,
            "email": self.email,
            "num_of_contributions": self.num_of_contributions,
            "spotify_refresh_token": self.spotify_refresh_token
        }
        return user

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def valid_email(email):
        emailPattern = re.compile("[^@]+@[^@]+\.[^@]+")
        if emailPattern.match(email) is None:
            return True
        return True

    @staticmethod
    def valid_username(username):
        usernamePattern = re.compile("^\w{1,255}$")
        if usernamePattern.match(username) is None:
            return True
        return True



class Lyrics(db.Model):
    __tablename__ = 'Lyrics'

    id = db.Column(db.Integer, primary_key=True)
    songtitle = db.Column(db.String(255), unique=False, nullable=False)
    artist = db.Column(db.String(255), unique=False, nullable=False)
    spotify_track_id = db.Column(db.String(255), unique=True, nullable=True)
    lyrics = db.Column(db.Text)
    timestamps = db.Column(db.Text)

    def __init__(self, songtitle, artist, spotify_track_id, lyrics, timestamps):
        self.songtitle = songtitle
        self.artist = artist
        self.spotify_track_id = spotify_track_id
        self.lyrics = lyrics
        self.timestamps = timestamps

    def __repr__(self):
        return 'id: {}, songtitle: {}, spotify_track_id: {}, lyrics: {}, timestamps: {}' \
            .format(self.id, self.songtitle, self.spotify_track_id, self.lyrics, self.timestamps)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def toJSON(self):
        lyric_sheet = {
            "songtitle": self.songtitle,
            "artist": self.artist,
            "spotify_track_id": self.spotify_track_id,
            "lyrics": self.lyrics,
            "timestamps": self.timestamps
        }
        return lyric_sheet

    @staticmethod
    def get_all():
        return Lyrics.query.all()
		
class LyricRating(db.Model):
    __tablename__ = 'LyricRating'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    lyrics_id = db.Column(db.Integer, db.ForeignKey('Lyrics.id', ondelete='CASCADE'), nullable=False)
    lyrics_id_rel = db.relationship('Lyrics', backref=db.backref('lyrics_id', passive_deletes=True),
                                    foreign_keys=lyrics_id)

    rater_id = db.Column(db.Integer, db.ForeignKey('Users.id', ondelete='CASCADE'), nullable=False)
    rater_id_rel = db.relationship('User', backref=db.backref('rater_id', passive_deletes=True), foreign_keys=rater_id)

    def __init__(self, rating, lyrics_id, rater_id):
        self.rating = rating
        self.lyrics_id = lyrics_id
        self.rater_id = rater_id

    def __repr__(self):
        return 'id: {}, rating: {}, lyrics_id: {}, rater_id: {}' \
            .format(self.id, self.rating, self.lyrics_id, self.rater_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def toJSON(self):
        rating = {
            "rating": self.rating,
            "lyrics_id": self.lyrics_id,
            "rater_id": self.rater_id
        }
        return rating

    @staticmethod
    def get_all():
        return LyricRating.query.all()


class RecentActivity(db.Model):
    __tablename__ = 'RecentActivity'

    id = db.Column(db.Integer, primary_key=True)
    spotify_track_id = db.Column(db.String(255), unique=False, nullable=False)
    spotify_id = db.Column(db.String(255), unique=False, nullable=False)

    def __init__(self, spotify_track_id, spotify_id):
        self.spotify_track_id = spotify_track_id
        self.spotify_id = spotify_id

    def __repr__(self):
        return 'id: {}, spotify_track_id: {}, spotify_id: {}' \
            .format(self.id, self.spotify_track_id, self.spotify_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def toJSON(self):
        rating = {
            "spotify_track_id": self.spotify_track_id,
            "spotify_id": self.spotify_id,
            "username": db.session.query(User).filter_by(spotify_id=self.spotify_id).first().username
        }
        return rating

    @staticmethod
    def get_all():
        return RecentActivity.query.all()

