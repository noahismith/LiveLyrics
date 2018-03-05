from flask import Blueprint, request, jsonify
from app.spotifyapi import *
from app import db
from .models import *
from sqlalchemy import and_

lyricrating_blueprint = Blueprint('lyricrating', __name__)


# TODO: add a rating

@lyricrating_blueprint.route("/rate", methods=['POST'])
def rate():
    payload = json.loads(request.data.decode())
    rating = payload['rating']
    lyrics_id = payload['lyric_id']
    rater_id = payload['rater_id']

    lyric_sheet = db.session.query(Lyrics).filter_by(spotify_track_id=lyrics_id).first()
    rater = db.session.query(User).filter_by(spotify_id=rater_id).first()

    if lyric_sheet is None:
        return jsonify({'result': False, 'error': "Lyric sheet not found in the database."})

    if rater is None:
        return jsonify({'result': False, 'error': "User not found in the database."})

    lyric_rating = db.session.query(LyricRating).filter(and_(LyricRating.lyrics_id == lyric_sheet.id, LyricRating.rater_id == rater.id)).first()

    if lyric_rating is None:
        lyric_rating = LyricRating(rating, lyric_sheet.id, rater.id)
        lyric_rating.save()
        return jsonify({'result': True, 'error': ""})

    lyric_rating.rating = rating
    lyric_rating.save()

    return jsonify({'result': True, 'error': ""})
	
@lyricrating_blueprint.route("/getRating", methods=['POST'])
def getRating():
    payload = json.loads(request.data.decode())
    lyrics_id = payload['lyric_id']
    rater_id = payload['rater_id']
	
    lyric_sheet = db.session.query(Lyrics).filter_by(spotify_track_id=lyrics_id).first()
    rater = db.session.query(User).filter_by(spotify_id=rater_id).first()


    if lyric_sheet is None:
        return jsonify({'result': False, 'error': "Lyric sheet not found in the database."})

    if rater is None:
	    return jsonify({'result': False, 'error': "User not found in the database."})

    lyric_rating = db.session.query(LyricRating).filter(and_(LyricRating.lyrics_id == lyric_sheet.id, LyricRating.rater_id == rater.id)).first()

    if lyric_rating is None:
        return jsonify({'result': False, 'error': "The user has not put a rating on this lyric page."})
		
    return jsonify({'result': True, 'error': "", "rating": lyric_rating.toJSON()})
	
@lyricrating_blueprint.route("/getRatings", methods=['POST'])
def getRatings():
    payload = json.loads(request.data.decode())
    lyrics_id = payload['lyric_id']
	
    lyric_sheet = db.session.query(Lyrics).filter_by(spotify_track_id=lyrics_id).first()
	
    if lyric_sheet is None:
        return jsonify({'result': False, 'error': "Lyric sheet not found in the database."})
	
    lyricRatings = db.session.query(LyricRating).filter(LyricRating.lyrics_id == lyric_sheet.id)
	
    if lyricRatings is None:
	    return jsonify({'result': False, 'error': "The requested lyrics page has no ratings."})
		
    allRatingsList = []
    for rating in lyricRatings:
	    allRatingsList.append(rating.toJSON())
		
    return jsonify({'result': True, 'error': "", 'ratings': allRatingsList})
	
@lyricrating_blueprint.route("/getUserRatings", methods=['POST'])
def getUserRatings():
    payload = json.loads(request.data.decode())
    rater_id = payload['rater_id']
    rater = db.session.query(User).filter_by(spotify_id=rater_id).first()

    if rater is None:
	    return jsonify({'result': False, 'error': "User not found in the database."})

    lyricRatings = db.session.query(LyricRating).filter(LyricRating.rater_id == rater.id)
	
    if lyricRatings is None:
	    return jsonify({'result': False, 'error': "The requested lyrics page has no ratings."})
		
    allRatingsList = []
    for rating in lyricRatings:
	    allRatingsList.append(rating.toJSON())
		
    return jsonify({'result': True, 'error': "", 'ratings': allRatingsList})

@lyricrating_blueprint.route("/getAllRatings", methods=['GET'])	
def getAllRatings():
    lyricRatings = LyricRating.get_all()
    ratings_list = []
    for rating in lyricRatings:
        ratings_list.append(rating.toJSON())
    return jsonify({'result': True, 'error': "", 'ratings': ratings_list})
        