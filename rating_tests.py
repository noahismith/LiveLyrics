import unittest
import json
from flask import make_response, redirect

import app
from app.models import User, LyricRating
from app import db

test_rating = { "songtitle": "Test",
              "rater_id": "wojtr",
              "lyrics_id": "4YwbSZaYeYja8Umyt222Qf",
              "rating": "1",
              "spotify_access_token": "BQDZKDDDV88rwz600LmpHvYXUI1QjOkTUPDOP7Rvn9dOEnkonBqAUTazy2SFPcNbzVcxv7NSPnyRBAcISeiLST1KSOfalaAu8EeI5TELzMwRgsBeg8spohPhj_SPO0YRnjvJ3_ls6MNKeZtIaFi6rLuaLost"
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
		
    def test_rate_bad_rater(self):
        with self.app.app_context():
		
            response = self.client.post('/lyricrating/rate', data=json.dumps(dict(rater_id="Bad User ID",
                                                                             lyric_id=test_rating["lyrics_id"],
                                                                             rating=test_rating["rating"])),
                                          content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error is not ""
            assert result is False

        return
		
    def test_rate_bad_lyric_page(self):
        with self.app.app_context():
		
            response = self.client.post('/lyricrating/rate', data=json.dumps(dict(rater_id=test_rating["rater_id"],
                                                                             lyric_id="Bad Lyric Page ID",
                                                                             rating=test_rating["rating"])),
                                          content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error is not ""
            assert result is False

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
		
    def test_rating_bad_rater(self):
        with self.app.app_context():
		
            response = self.client.post('/lyricrating/getRating', data=json.dumps(dict(rater_id="Bad User ID",
                                                                             lyric_id=test_rating["lyrics_id"],
                                                                             rating=test_rating["rating"])),
                                          content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error is not ""
            assert result is False

        return
		
    def test_rating_bad_lyric_page(self):
        with self.app.app_context():
		
            response = self.client.post('/lyricrating/getRating', data=json.dumps(dict(rater_id=test_rating["rater_id"],
                                                                             lyric_id="Bad Lyric Page ID",
                                                                             rating=test_rating["rating"])),
                                          content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error is not ""
            assert result is False

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
		
    def test_ratings_bad_lyric_page(self):
        with self.app.app_context():
		
            response = self.client.post('/lyricrating/getRatings', data=json.dumps(dict(rater_id=test_rating["rater_id"],
                                                                             lyric_id="Bad Lyric Page ID",
                                                                             rating=test_rating["rating"])),
                                          content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error is not ""
            assert result is False

        return
		
    def test_user_ratings(self):
        with self.app.app_context():

            response = self.client.post('/lyricrating/getUserRatings', data=json.dumps(dict(rater_id=test_rating["rater_id"],
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
		
    def test_user_ratings_bad_rater(self):
        with self.app.app_context():
		
            response = self.client.post('/lyricrating/getUserRatings', data=json.dumps(dict(rater_id="Bad User ID",
                                                                             lyric_id=test_rating["lyrics_id"],
                                                                             rating=test_rating["rating"])),
                                          content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error is not ""
            assert result is False

        return
		

    def tearDown(self):
        return


if __name__ == '__main__':
    unittest.main()