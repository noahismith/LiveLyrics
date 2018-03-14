import unittest
import json
from flask import make_response, redirect

import app
from app.models import User, Lyrics
from app import db

test_lyric_page = { "songtitle": "Test",
              "spotify_track_id": "00pLvXMdSXJG8HLliuWTWt",
              "lyrics": "Test",
              "timestamps": "Test",
              "spotify_access_token": "BQABD8DYF_yV9w7noz53rgMB0K7q8Fd0x5bVHEwPqHttnVujRbRfEXWYbiDFfqbsJdc-3RNOBd5ToujyFRj5WRexe3KagUfjRyDm09U21k2tqO72WKWP9w1uqo-sd0sjWKuR9Sxb4Vk265ff7JrJ2x6KzGQy"
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
            assert temp_lyrics is not None

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
            assert temp_lyrics is not None

            id = temp_lyrics.id

            response = self.client.post('/lyrics/lyrics_page', data=json.dumps(dict(songtitle=test_lyric_page["songtitle"],
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
            assert temp_lyrics is not None

            id = temp_lyrics.id
            search_string = "Hello"

            response = self.client.post('/lyrics/search', data=json.dumps(dict(songtitle=test_lyric_page["songtitle"],
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
		
    def test_lyrics_dont_exist(self):
        with self.app.app_context():

            temp_lyrics = db.session.query(Lyrics).filter_by(spotify_track_id="Test").first()
            assert temp_lyrics is None

            response = self.client.post('/lyrics/lyrics_page', data=json.dumps(dict(songtitle=test_lyric_page["songtitle"],
                                                                             spotify_track_id=test_lyric_page["spotify_track_id"],
                                                                             lyrics=test_lyric_page["lyrics"],
																			 timestamps=test_lyric_page["timestamps"])),
                                          content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error is ""
            assert result is True
			
    def test_lyrics_overwiten(self):
        with self.app.app_context():

            temp_lyrics = db.session.query(Lyrics).filter_by(spotify_track_id=test_lyric_page["spotify_track_id"]).first()
            assert temp_lyrics is not None

            id = temp_lyrics.id

            response = self.client.post('/lyrics/edit', data=json.dumps(dict(songtitle=test_lyric_page["songtitle"],
                                                                             spotify_track_id=test_lyric_page["spotify_track_id"],
                                                                             lyrics="New Lyrics",
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
            assert temp_lyrics.lyrics == "New Lyrics"
            assert temp_lyrics.timestamps == test_lyric_page["timestamps"]
        return

    def tearDown(self):
        return


if __name__ == '__main__':
    unittest.main()