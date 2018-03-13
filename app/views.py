from flask import Blueprint, render_template, redirect, request, make_response, url_for, jsonify
import urllib
from app.spotifyapi import *
import app

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



