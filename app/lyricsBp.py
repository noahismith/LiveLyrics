from flask import Blueprint, request, jsonify
from .models import *
from .spotifyapi import *

lyrics_blueprint = Blueprint('lyrics', __name__)


@lyrics_blueprint.route("/edit", methods=['POST'])
def edit():
	payload = json.loads(request.data.decode())
	songtitle = payload["songtitle"]
	spotify_track_id = payload["spotify_track_id"]
	lyrics = payload["lyrics"]
	timestamps = payload["timestamps"]
	access_token = payload['access_token']

	spotify_info = get_profile_me(access_token)
	if "error" in spotify_info:
		return jsonify({'result': False, 'error': spotify_info['error']})
	spotify_id = spotify_info['id']

	user = db.session.query(User).filter_by(spotify_id=spotify_id).first()

	lyrics_page = db.session.query(Lyrics).filter_by(spotify_track_id=spotify_track_id).first()

	if user is None:
		return jsonify({'result': False, 'error': "User not found"})

	if lyrics_page is None:
		return jsonify({'result': False, 'error': 'No Knone Lyrics Page'})

	lyrics_page.songtitle = songtitle
	lyrics_page.spotify_track_id = spotify_track_id
	lyrics_page.lyrics = lyrics
	lyrics_page.timestamps = timestamps
	user.num_of_contributions = user.num_of_contributions + 1
	db.session.commit()
  
	return jsonify({'result': True, 'error': ""})


@lyrics_blueprint.route("/lyrics_page", methods=['POST'])
def get_lyrics():
    payload = json.loads(request.data.decode())
    access_token = payload['access_token']
    spotify_track_id = payload["spotify_track_id"]

    spotify_info = get_profile_me(access_token)
    if "error" in spotify_info:
        return jsonify({'result': False, 'error': spotify_info['error']})
    spotify_id = spotify_info['id']

    lyrics_page = db.session.query(Lyrics).filter_by(spotify_track_id=spotify_track_id).first()

    if lyrics_page is None:
        spotify_track = get_track(access_token, spotify_track_id)
        if "error" in spotify_track:
            return jsonify({'result': False, 'error': spotify_track['error']})
        track_name = spotify_track['name']
        lyrics_page = Lyrics(track_name, spotify_track_id, "", "")
        lyrics_page.save()
        return jsonify({'result': True, 'error': 'Page added', 'lyric_page': lyrics_page.toJSON()})

    return jsonify({'result': True, 'error': "", 'lyric_page': lyrics_page.toJSON()})

@lyrics_blueprint.route("/getAll", methods=['GET'])
def getAllLyricPages():
    lyric_pages = Lyrics.get_all()
    lyric_pages_list = []
    for lyric_page in lyric_pages:
        lyric_pages_list.append(lyric_page.toJSON())
    return jsonify({'result': True, 'error': "", 'lyric_pages': lyric_pages_list})

@lyrics_blueprint.route("/search", methods=['POST'])
def search():
    payload = json.loads(request.data.decode())
    access_token = payload['access_token']
    search_string = payload['search_string']
    
    resp = search_track(access_token, search_string)
    if "error" in resp:
        return jsonify({'result': False, 'error': resp['error']})
    tracks = resp['tracks']['items']
	
    artists = (search_artist(access_token, search_string))['artists']['items']

    for track in tracks:
        spotify_track_id = track['id']
        if db.session.query(Lyrics).filter_by(spotify_track_id=spotify_track_id) is not None:
            continue
        track_name = track['name']
        spotify_track_id = track['id']
        lyrics_page = db.session.query(Lyrics).filter_by(spotify_track_id=spotify_track_id).first()
        if lyrics_page is None :
            artist = get_artist_by_track(track)
            lyrics_page = Lyrics(track_name, artist, spotify_track_id, "", "")
            lyrics_page.save()

    lyric_sheets = db.session.query(Lyrics).filter(Lyrics.songtitle.like("%{}%".format(search_string))).all()

    lyric_sheets_list = []
    for lyric_sheet in lyric_sheets:
	    lyric_sheets_list.append(lyric_sheet.toJSON())
	
    artists_list = []
    for artist in artists:
        artists_list.append({
            'name': artist['name'],
            'id': artist['id']
            })

    return jsonify({'result': True, 'error': "", 'lyric_sheets': lyric_sheets_list, 'artists': artists_list})
