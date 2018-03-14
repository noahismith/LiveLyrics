import unittest
import json
from flask import make_response, redirect

import app
from app.models import User, LyricRating
from app import db

test_rating = { "songtitle": "Test",
              "rater_id": "wojtr",
              "lyrics_id": "00pLvXMdSXJG8HLliuWTWt",
              "rating": "1",
              "spotify_access_token": "BQABD8DYF_yV9w7noz53rgMB0K7q8Fd0x5bVHEwPqHttnVujRbRfEXWYbiDFfqbsJdc-3RNOBd5ToujyFRj5WRexe3KagUfjRyDm09U21k2tqO72WKWP9w1uqo-sd0sjWKuR9Sxb4Vk265ff7JrJ2x6KzGQy"
}

class TestRatings(unittest.TestCase):

    def setUp(self):
        self.app = app.create_app("development")
        self.client = self.app.test_client(use_cookies=True)

        self.client.set_cookie("http://127.0.0.1:5000/", "access_token", test_rating["spotify_access_token"])

        with self.app.app_context():
            db.create_all()

    def test_rate(self):
        with self.app.app_context():
		
            response = self.client.post('/lyricrating/rate', data=json.dumps(dict(rater_id=test_rating["rater_id"],
                                                                             lyric_id=test_rating["lyrics_id"],
                                                                             rating=test_rating["rating"])),
                                          content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error == ""
            assert result is True

        return

    def test_rating(self):
        with self.app.app_context():

            response = self.client.post('/lyricrating/getRating', data=json.dumps(dict(rater_id=test_rating["rater_id"],
                                                                             lyric_id=test_rating["lyrics_id"],
                                                                             rating=test_rating["rating"])),
                                          content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error == ""
            assert result is True
            assert "rating" in resp
        return
		
    def test_ratings(self):
        with self.app.app_context():

            response = self.client.post('/lyricrating/getRatings', data=json.dumps(dict(rater_id=test_rating["rater_id"],
                                                                             lyric_id=test_rating["lyrics_id"],
                                                                             rating=test_rating["rating"])),
                                          content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error == ""
            assert result is True
            assert "ratings" in resp

        return
		
    def test_user_ratings(self):
        with self.app.app_context():

            response = self.client.post('/lyricrating/getRatings', data=json.dumps(dict(rater_id=test_rating["rater_id"],
                                                                             lyric_id=test_rating["lyrics_id"],
                                                                             rating=test_rating["rating"])),
                                          content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error == ""
            assert result is True
            assert "ratings" in resp

        return
		

    def tearDown(self):
        return


if __name__ == '__main__':
    unittest.main()