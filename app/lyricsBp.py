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
    search_string = payload['search_string']

    lyric_sheets = db.session.query(Lyrics).filter(Lyrics.songtitle.like("%{}%".format(search_string))).all()

    lyric_sheets_list = []
    for lyric_sheet in lyric_sheets:
        lyric_sheets_list.append(lyric_sheet.toJSON)


    # TODO: look up string in our database return. If not there look in spotify, create new datbase entry else display error
    return