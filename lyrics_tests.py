import unittest
import json
from flask import make_response, redirect

import app
from app.models import User, Lyrics
from app import db

test_lyric_page = { "songtitle": "Test",
              "spotify_track_id": "lnxd0zmjpsimn9mivdad7o9sh",
              "lyrics": "Test",
              "timestamps": "Test",
              "spotify_access_token": "BQCpoX9BeHL8QS5i73KAhVtCdJGljgcqQ34hJJieDsGoIsv7nPJRrzNe0fHw5DmeZj_I9IIwQcb-GKIcPw5AwiKks7AImHVKTB1ZWJMHiLD37LGsZ3MzKliVjCEh_nPH_qFTScMCgDg1Zi88teglZ5wD63lDPTIJSSiQVND_ekotutQq1fs"
}

class TestLyrics(unittest.TestCase):

    def setUp(self):
        self.app = app.create_app("development")
        self.client = self.app.test_client(use_cookies=True)

        self.client.set_cookie("http://127.0.0.1:5000/", "access_token", test_lyric_page["spotify_access_token"])

        with self.app.app_context():
            db.create_all()

    def test_lyrics_edit(self):
        with self.app.app_context():

            temp_lyrics = db.session.query(Lyrics).filter_by(spotify_track_id=test_lyric_page["spotify_track_id"]).first()
            assert temp_lyrics in db.session

            id = temp_lyrics.id

            response = self.client.post('/lyrics/edit', data=json.dumps(dict(songtitle=test_lyric_page["songtitle"],
                                                                             spotify_track_id=test_lyric_page["spotify_track_id"],
                                                                             lyrics=test_lyric_page["lyrics"],
																			 timestamps=test_lyric_page["timestamps"])),
                                          content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error == ""
            assert result is True

            temp_lyrics = db.session.query(Lyrics).filter_by(id=id).first()

            assert temp_lyrics.songtitle == test_lyric_page["songtitle"]
            assert temp_lyrics.spotify_track_id == test_lyric_page["spotify_track_id"]
            assert temp_lyrics.lyrics == test_lyric_page["lyrics"]
            assert temp_lyrics.timestamps == test_lyric_page["timestamps"]
        return

    def test_lyrics_get(self):
        with self.app.app_context():

            temp_lyrics = db.session.query(Lyrics).filter_by(spotify_track_id=test_lyric_page["spotify_track_id"]).first()
            assert temp_lyrics in db.session

            id = temp_lyrics.id

            response = self.client.post('/lyrics/edit', data=json.dumps(dict(songtitle=test_lyric_page["songtitle"],
                                                                             spotify_track_id=test_lyric_page["spotify_track_id"],
                                                                             lyrics=test_lyric_page["lyrics"],
																			 timestamps=test_lyric_page["timestamps"])),
                                          content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error == ""
            assert result is True

            temp_lyrics = db.session.query(Lyrics).filter_by(id=id).first()

            assert temp_lyrics.songtitle == resp['lyric_page']['songtitle']
            assert temp_lyrics.spotify_track_id == resp['lyric_page']["spotify_track_id"]
            assert temp_lyrics.lyrics == resp['lyric_page']["lyrics"]
            assert temp_lyrics.timestamps == resp['lyric_page']["timestamps"]
        return
		
    def test_lyrics_search(self):
        with self.app.app_context():

            temp_lyrics = db.session.query(Lyrics).filter_by(spotify_track_id=test_lyric_page["spotify_track_id"]).first()
            assert temp_lyrics in db.session

            id = temp_lyrics.id
            search_string = "Hello"

            response = self.client.post('/lyrics/edit', data=json.dumps(dict(songtitle=test_lyric_page["songtitle"],
                                                                             spotify_track_id=test_lyric_page["spotify_track_id"],
                                                                             lyrics=test_lyric_page["lyrics"],
																			 timestamps=test_lyric_page["timestamps"],
																			 search_string = search_string)),
                                          content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error == ""
            assert result is True
            assert 'lyric_sheets' in resp
            assert 'artists' in resp

        return

    def tearDown(self):
        return


if __name__ == '__main__':
    unittest.main()