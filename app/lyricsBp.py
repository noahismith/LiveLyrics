from flask import Blueprint, request, jsonify
from app.spotifyapi import *
from app import db
from .models import *
import requests

lyrics_blueprint = Blueprint('lyrics', __name__)

# TODO: add/edit lyrics
@lyrics_blueprint.route("/edit", methods=['POST'])
def edit():
	payload = json.loads(request.data.decode())
	songtitle = payload["songtitle"]
	spotify_track_id = payload["spotify_track_id"]
	lyrics = payload["lyrics"]
	timestamps = payload["timestamps"]
	access_token = payload['access_token']
	
	spotify_info = get_profile_me(access_token)
	spotify_id = spotify_info['id']
	
	if "error" in spotify_info:
		return jsonify({'result': False, 'error': spotify_info['error']})
		
	user = db.session.query(User).filter_by(spotify_id=spotify_id).first()
	
	lyrics_page = db.session.query(Lyrics).filter_by(spotify_track_id=spotify_track_id).first()
	
	if lyrics_page is None:
		return jsonify({'result': False, 'error': 'No Knone Lyrics Page'})
	
	lyrics_page.songtitle = songtitle
	lyrics_page.spotify_track_id = spotify_track_id
	lyrics_page.lyrics = lyrics
	lyrics_page.timestamps = timestamps
	user.num_of_contributions = user.num_of_contributions + 1
	db.session.commit()
	
# TODO: add/edit timestamps	
# TODO: get lyric sheet
@lyrics_blueprint.route("/lyrics_page", methods=['POST'])
def get_lyrics():
	payload = json.loads(request.data.decode())
	access_token = payload['access_token']
	spotify_track_id = payload["spotify_track_id"]

	spotify_info = get_profile_me(access_token)
	spotify_id = spotify_info['id']
	
	if "error" in spotify_info:
		return jsonify({'result': False, 'error': spotify_info['error']})
		
	user = db.session.query(User).filter_by(spotify_id=spotify_id).first()
	
	lyrics_page = db.session.query(Lyrics).filter_by(spotify_track_id=spotify_track_id).first()
	
	if lyrics_page is None:
		return jsonify({'result': False, 'error': 'No Knone Lyrics Page'})
		
	return jsonify({'result': True, 'error': "", 'lyric_page': lyrics_page.toJSON()})
	
	
# TODO: look up lyrics sheet
# TODO: create


@lyrics_blueprint.route("/search", methods=['POST'])
def search():
    payload = json.loads(request.data.decode())
    search_string = payload['search_string']

    lyric_sheets = db.session.query(Lyrics).filter(Lyrics.songtitle.like("%{}%".format(search_string))).all()

    lyric_sheets_list = []
    for lyric_sheet in lyric_sheets:
        lyric_sheets_list.append(lyric_sheet.toJSON)


    # TODO: look up string in our database return. If not there look in spotify, create new datbase entry else display error
    return