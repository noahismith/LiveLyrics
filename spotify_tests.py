import unittest
import json
from flask import make_response, redirect
from datetime import datetime

import app
from app.models import User, Lyrics
from app.spotifyapi import *
from app import db

spotify_access_token = "BQBDlcIjEQaFWTuEmhyJMs5iIumK84xvA-RFlWbAhpLEVzutNT1yx7OOly6ThBl9KIONAT5uH2IxQdHWbJrtu-leOPkFlRtdI-Dhb2ZWBSXslGqaJNAlkzz1XRwk_9iuJPN1NeaWL1L7NcopO_5yE-cmxW8jtJd6wn9Kcx0TuYN6psQHGFQ"

test_user = { "username": "",
              "spotify_id": "",
              "birthdate": "",
              "email": "",
              "spotify_access_token": spotify_access_token,
              "spotify_refresh_token": ""
}

class TestSpotifyAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.create_app("development")
        self.client = self.app.test_client(use_cookies=True)

        with self.app.app_context():
            self.client.set_cookie("http://127.0.0.1:5000/", "access_token", spotify_access_token)
            response = self.client.post('/users/info/me', data=json.dumps(dict()), content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']
            user = resp['user']

            test_user['username'] = user['username']
            test_user['spotify_id'] = user['spotify_id']
            test_user["birthdate"] = user['birthdate']
            test_user['email'] = user['email']
            test_user['spotify_refresh_token'] = user['spotify_refresh_token']

            db.create_all()

    def test_spotify_get_profile_me(self):
        with self.app.app_context():
            spotify_info = get_profile_me(spotify_access_token)

            username = spotify_info['display_name'] if spotify_info['display_name'] is not None else spotify_info['id']
            spotify_id = spotify_info['id']
            email = spotify_info['email']

            assert test_user['username'] == username
            assert test_user['spotify_id'] == spotify_id
            assert test_user['email'] == email
        return

    def test_spotify_search_track(self):
        search_string = "1-800-273-8255"
        songtilte = "1-800-273-8255"
        spotify_track_id = "5tz69p7tJuGPeMGwNTxYuV"
        artists = "Logic, Alessia Cara, Khalid"
        with self.app.app_context():
            spotify_track = search_track(spotify_access_token, search_string)
            query_track = spotify_track['tracks']['items'][0]
            query_songtitle = query_track['name']
            query_spotify_track_id = query_track['id']
            query_artists = get_artists_by_track(query_track)

            assert songtilte == query_songtitle
            assert query_spotify_track_id == spotify_track_id
            assert query_artists == artists
        return

    def test_spotify_search_track_spaces(self):
        search_string = "The Soundtrack to Missing a Slam Dunk"
        songtilte = "The Soundtrack To Missing A Slam Dunk"
        spotify_track_id = "2ETF2hAOqRDcNfuEfYRgcK"
        artists = "Hot Mulligan"
        with self.app.app_context():
            spotify_track = search_track(spotify_access_token, search_string)
            query_track = spotify_track['tracks']['items'][0]
            query_songtitle = query_track['name']
            query_spotify_track_id = query_track['id']
            query_artists = get_artists_by_track(query_track)

            assert songtilte == query_songtitle
            assert query_spotify_track_id == spotify_track_id
            assert query_artists == artists
        return

    def test_spotify_search_artist(self):
        search_string = "1-800-273-8255"
        songtilte = "1-800-273-8255"
        spotify_track_id = "5tz69p7tJuGPeMGwNTxYuV"
        artists = "Logic, Alessia Cara, Khalid"
        with self.app.app_context():
            spotify_track = search_track(spotify_access_token, search_string)
            query_track = spotify_track['tracks']['items'][0]
            query_artists = get_artists_by_track(query_track)

            assert query_artists == artists
        return

    def test_spotify_get_track(self):
        search_string = "1-800-273-8255"
        songtilte = "1-800-273-8255"
        spotify_track_id = "5tz69p7tJuGPeMGwNTxYuV"
        artists = "Logic, Alessia Cara, Khalid"
        with self.app.app_context():
            spotify_track = get_track(spotify_access_token, spotify_track_id)
            query_songtitle = spotify_track['name']
            query_spotify_track_id = spotify_track['id']
            query_artists = get_artists_by_track(spotify_track)

            assert songtilte == query_songtitle
            assert query_spotify_track_id == spotify_track_id
            assert query_artists == artists
        return

    def test_spotify_invalid_token(self):
        invalid_token = "invalid_token"
        with self.app.app_context():
            resp = get_profile_me(invalid_token)
            assert resp["error"]['message'] == "Invalid access token"
            resp = search_track(invalid_token, "search string")
            assert resp["error"]['message'] == "Invalid access token"
            resp = search_artist(invalid_token, "search string")
            assert resp["error"]['message'] == "Invalid access token"
            resp = get_track(invalid_token, "track id")
            assert resp["error"]['message'] == "Invalid access token"
        return

    def tearDown(self):
        return


if __name__ == '__main__':
    unittest.main()