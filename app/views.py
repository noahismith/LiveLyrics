from flask import Blueprint, render_template, redirect, request, make_response, url_for, jsonify
import urllib
from app.spotifyapi import *
import app

views_blueprint = Blueprint('views', __name__)

@views_blueprint.route("/")
def index():
    return render_template('index.html')


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


@views_blueprint.route("/oauth")
def oauth():
    url_args = "&".join(["{}={}".format(key, urllib.quote(val)) for key, val in auth_query_parameters.iteritems()])
    auth_url = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)
    return redirect(auth_url)


@views_blueprint.route("/login", methods=['POST'])
def login():
   payload = json.loads(request.data.decode())
   code = payload['code']

   #code = request.args.get('code')
   tokens = get_tokens(code)

   access_token = tokens["access_token"]
   refresh_token = tokens["refresh_token"]
   token_type = tokens["token_type"]
   expires_in = tokens["expires_in"]

   app.usersBp.login(access_token, refresh_token)

   return jsonify({"result": True, "error": "", "access_token": access_token})


@views_blueprint.route("/callback")
def callback():
    if "error" in request.query_string:
        return make_response(redirect(url_for("index")))

    return redirect(url_for("views.index"))



