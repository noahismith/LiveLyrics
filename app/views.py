from flask import Blueprint, render_template, redirect, request, make_response, url_for, jsonify
import urllib
from app.spotifyapi import *
import app
from app import db
from models import *

views_blueprint = Blueprint('views', __name__)

@views_blueprint.route("/")
def index():
    auth_url = get_auth_url()
    return render_template('index.html', auth_url=auth_url)


@views_blueprint.route("/lyrics")
def lyrics():
    return render_template('lyrics.html')


@views_blueprint.route("/users")
def users():
    return render_template("users.html")


@views_blueprint.route("/songs")
def songs():
    return render_template("songs.html")


@views_blueprint.route("/contact")
def contact():
    return render_template("contact.html")


@views_blueprint.route("/login")
def login():
    code = request.args['code']

    tokens = get_tokens(code)

    if "error" in tokens:
        return redirect(url_for("views.index"))

    access_token = tokens["access_token"]
    refresh_token = tokens["refresh_token"]
    token_type = tokens["token_type"]
    ##expires_in = tokens["expires_in"]

    app.usersBp.login(access_token, refresh_token)

    resp = make_response(redirect(url_for("views.index")))
    resp.set_cookie('access_token', access_token)

    return resp

@views_blueprint.route("/currSong", methods=['POST'])
def get_current_track_id():
   access_token = request.cookies.get('access_token')

   authorization_header = {"Authorization": "Bearer {}".format(access_token)}
   current_playing_api_endpoint = "{}/me/player/currently-playing".format(SPOTIFY_API_URL)
   current_playing_object = requests.get(current_playing_api_endpoint, headers=authorization_header)
   if "error" in json.loads(current_playing_object.text):
       return jsonify({'result': False, 'error': json.loads(current_playing_object.text)["error"]})
   spotify_track_id = json.loads(current_playing_object.text)['item']['id']
   lyrics_page = db.session.query(Lyrics).filter_by(spotify_track_id=spotify_track_id).first()
   if lyrics_page is None:
       track_name = json.loads(current_playing_object.text)['item']['name']
       artist = get_artists_by_track(json.loads(current_playing_object.text)['item'])
       lyrics_page = Lyrics(track_name, artist, spotify_track_id, "", "")
       lyrics_page.save()    
   return jsonify({'result': True, 'error': "", 'lyric_page': lyrics_page.toJSON()})