from flask import Blueprint, request, jsonify
from app.spotifyapi import *
from app import db
from .models import *

users_blueprint = Blueprint('users', __name__)


def login(access_token, refresh_token):
    spotify_info = get_profile_me(access_token)

    if "error" in spotify_info:
        return spotify_info['error']

    username = spotify_info['display_name'] if spotify_info['display_name'] is not None else spotify_info['id']
    spotify_id = spotify_info['id']
    birthdate = spotify_info['birthdate']
    email = spotify_info['email']

    user = db.session.query(User).filter_by(spotify_id=spotify_id).first()
    if user is not None:
        user.spotify_refresh_token = refresh_token
        return

    new_user = User(username, spotify_id, birthdate, email, refresh_token)
    new_user.save()
    return

# Requires login
@users_blueprint.route("/edit", methods=['POST'])
def edit():
    payload = json.loads(request.data.decode())
    access_token = payload['access_token']
    username = payload['username']
    birthdate = payload['birthdate']
    email = payload['email']

    spotify_info = get_profile_me(access_token)
    spotify_id = spotify_info['id']

    if "error" in spotify_info:
        return jsonify({'result': False, 'error': spotify_info['error']})

    user = db.session.query(User).filter_by(spotify_id=spotify_id).first()

    if user is None:
        return jsonify({'result': False, 'error': "User does not exist"})

    # TODO: check error where username or email are not unique
    # TODO: POSSIBLY provide ability to change spotify id
    user.username = username
    user.birthdate = birthdate
    user.email = email
    user.save()

    return jsonify({ 'result': True, 'error': ""})


@users_blueprint.route("/info", methods=['POST'])
def info():
    print(request)
    payload = json.loads(request.data.decode())
    username = payload['username']

    user = db.session.query(User).filter_by(username=username).first()

    if user is None:
        return jsonify({'result': False, 'error': "User does not exist"})

    return jsonify({'result': True, 'error': "", 'user': user.toJSON()})


@users_blueprint.route("/all", methods=['GET'])
def getall():

    all_users = User.get_all()
    all_users_list = []
    for user in all_users:
        all_users_list.append(user.toJSON())

    return jsonify({'result': True, 'error': "", 'users': all_users_list})
