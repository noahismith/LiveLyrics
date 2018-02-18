from flask import Blueprint, request, jsonify
from app.spotifyapi import *
from app import db
from .models import *

lyrics_blueprint = Blueprint('lyrics', __name__)

# TODO: add/edit lyrics
# TODO: add/edit timestamps
# TODO: get lyric sheet
# TODO: look up lyrics sheet
# TODO: create


@lyrics_blueprint.route("/search", methods=['POST'])
def search():
    payload = json.loads(request.data.decode())
    access_token = payload['access_token']
    search_string = payload['search_string']

    resp = search_track(access_token, search_string)
    print(resp)
    #tracks = resp['item']


    #for track in tracks:
    #    print(track)



    # Parse JSON string and add

    lyric_sheets = db.session.query(Lyrics).filter(Lyrics.songtitle.like("%{}%".format(search_string))).all()

    lyric_sheets_list = []
    for lyric_sheet in lyric_sheets:
        lyric_sheets_list.append(lyric_sheet.toJSON())

    # TODO: search spotify and return all results and add them to the database


    return jsonify({'result': True, 'error': "", 'lyric_sheets': lyric_sheets_list})
