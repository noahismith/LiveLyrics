import unittest
import json
from flask import make_response, redirect
import datetime

import app
from app.models import User
from app import db

spotify_access_token = "BQBDlcIjEQaFWTuEmhyJMs5iIumK84xvA-RFlWbAhpLEVzutNT1yx7OOly6ThBl9KIONAT5uH2IxQdHWbJrtu-leOPkFlRtdI-Dhb2ZWBSXslGqaJNAlkzz1XRwk_9iuJPN1NeaWL1L7NcopO_5yE-cmxW8jtJd6wn9Kcx0TuYN6psQHGFQ"

test_user = { "username": "",
              "spotify_id": "",
              "birthdate": "",
              "email": "",
              "spotify_access_token": spotify_access_token,
              "spotify_refresh_token": ""
}

class TestUsers(unittest.TestCase):

    def setUp(self):
        self.app = app.create_app("development")
        self.client = self.app.test_client(use_cookies=True)

        with self.app.app_context():
            self.client.set_cookie("http://127.0.0.1:5000/", "access_token", spotify_access_token)
            response = self.client.post('/users/info/me', data=json.dumps(dict()), content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            if resp['error'] != "":
                print("Please get a new access token")
            user = resp['user']

            test_user['username'] = user['username']
            test_user['spotify_id'] = user['spotify_id']
            test_user["birthdate"] = datetime.datetime.strptime(user['birthdate'], '%a, %d %b %Y %H:%M:%S GMT')
            test_user['email'] = user['email']
            test_user['spotify_refresh_token'] = user['spotify_refresh_token']
            db.create_all()

    def test_user_edit(self):
        edited_username = "TestUserNotInTheDatabase"
        edited_birthdate = "2012-11-06"
        edited_email = "TestUserEmailNotInTheDatabase@fakeWebsite.com"
        with self.app.app_context():

            temp_user = db.session.query(User).filter_by(spotify_id=test_user["spotify_id"]).first()
            assert temp_user in db.session

            id = temp_user.id

            response = self.client.post('/users/edit', data=json.dumps(dict(username=edited_username,
                                                                             birthdate=edited_birthdate,
                                                                             email=edited_email)),
                                          content_type='application/json')

            resp = json.loads(response.data.decode())
            print(resp)
            error = resp['error']
            result = resp['result']

            assert error == ""
            assert result is True

            temp_user = db.session.query(User).filter_by(id=id).first()

            assert temp_user.username == edited_username
            assert temp_user.email == edited_email

            temp_user.username = test_user['username']
            temp_user.birthdate = test_user['birthdate']
            temp_user.email = test_user['email']
            temp_user.save()

    def test_user_edit_blank_entries(self):
        with self.app.app_context():

            temp_user = db.session.query(User).filter_by(spotify_id=test_user["spotify_id"]).first()
            assert temp_user in db.session

            id = temp_user.id

            response = self.client.post('/users/edit', data=json.dumps(dict(username="",
                                                                             birthdate="",
                                                                             email="")),
                                        content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error == ""
            assert result is True

            temp_user_querry = db.session.query(User).filter_by(id=id).first()

            assert temp_user_querry.username == temp_user.username
            assert temp_user_querry.birthdate == temp_user.birthdate
            assert temp_user_querry.email == temp_user.email
        return

    def test_user_edit_username_special_char(self):
        with self.app.app_context():

            temp_user = db.session.query(User).filter_by(spotify_id=test_user["spotify_id"]).first()
            assert temp_user in db.session

            id = temp_user.id

            response = self.client.post('/users/edit', data=json.dumps(dict(username="TestU$er",
                                                                            birthdate="",
                                                                            email="")),
                                        content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error == "Invalid username"
            assert result is False

            temp_user.username = test_user['username']
            temp_user.save()
        return

    def test_user_edit_username_spaces(self):
        with self.app.app_context():

            temp_user = db.session.query(User).filter_by(spotify_id=test_user["spotify_id"]).first()
            assert temp_user in db.session

            id = temp_user.id

            response = self.client.post('/users/edit', data=json.dumps(dict(username="Test User",
                                                                            birthdate="",
                                                                            email="")),
                                        content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error == "Invalid username"
            assert result is False

            temp_user.username = test_user['username']
            temp_user.save()
        return

    def test_user_edit_max_length(self):
        username_max_length = "1HuM5RVKwL8FoqKPwt0pMcW0EXuJxwjhqEmnwJrNugW4x7P13EGRgJZVFURBEiyJOars0Ra6O5s0fUqeylWpr" \
                              "WGcyIQ8OvDHCeEe39WeSqb0vS0bHMhzRjcGTidOmLhgm2iZT8vJMblLLnRfyf02G6BWyT9EV2j5bdhF9dbE86" \
                              "10fGdwYnq1vhicBxgnrzgOF1VC5AlDXUopHAQeoWDzU6YVcnypdQsLOiW8akf2LUxL45Dhp9DYemyn38bciip"

        with self.app.app_context():
            temp_user = db.session.query(User).filter_by(spotify_id=test_user["spotify_id"]).first()
            assert temp_user in db.session

            id = temp_user.id

            response = self.client.post('/users/edit', data=json.dumps(dict(username=username_max_length,
                                                                            birthdate="",
                                                                            email="")),
                                        content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error == ""
            assert result is True

            temp_user = db.session.query(User).filter_by(id=id).first()

            assert temp_user.username == username_max_length

            temp_user.username = test_user['username']
            temp_user.save()
        return

    def test_user_edit_max_length_plus(self):
        username_max_length_plus = "1HuM5RVKwL8FoqKPwt0pMcW0EXuJxwjhqEmnwJrNugW4x7P13EGRgJZVFURBEiyJOars0Ra6O5s0fUqeylWpr" \
                              "WGcyIQ8OvDHCeEe39WeSqb0vS0bHMhzRjcGTidOmLhgm2iZT8vJMblLLnRfyf02G6BWyT9EV2j5bdhF9dbE86" \
                              "10fGdwYnq1vhicBxgnrzgOF1VC5AlDXUopHAQeoWDzU6YVcnypdQsLOiW8akf2LUxL45Dhp9DYemyn38bciip1"

        with self.app.app_context():
            temp_user = db.session.query(User).filter_by(spotify_id=test_user["spotify_id"]).first()
            assert temp_user in db.session

            id = temp_user.id

            response = self.client.post('/users/edit', data=json.dumps(dict(username=username_max_length_plus,
                                                                            birthdate="",
                                                                            email="")),
                                        content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error == "Invalid username"
            assert result is False

            temp_user = db.session.query(User).filter_by(id=id).first()

            assert temp_user.username != username_max_length_plus

            temp_user.username = test_user['username']
            temp_user.save()
        return

    def test_user_edit_duplicate_username(self):
        with self.app.app_context():
            temp_user = db.session.query(User).all()
            temp_user = temp_user[0]

            response = self.client.post('/users/edit', data=json.dumps(dict(username=temp_user.username,
                                                                            birthdate="",
                                                                            email="")),
                                        content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error == "Invalid username"
            assert result is False
        return

    def test_user_edit_duplicate_email(self):
        with self.app.app_context():
            temp_user = db.session.query(User).all()
            temp_user = temp_user[0]

            response = self.client.post('/users/edit', data=json.dumps(dict(username="",
                                                                            birthdate="",
                                                                            email=temp_user.email)),
                                        content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error == "Invalid email"
            assert result is False
        return

    def test_user_info(self):
        with self.app.app_context():
            temp_user = db.session.query(User).all()
            temp_user = temp_user[0]
            id = temp_user.id

            response = self.client.post('/users/info', data=json.dumps(dict(username=temp_user.username)),
                                        content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error == ""
            assert result is True

            user = resp['user']

            temp_user_query = db.session.query(User).filter_by(id=id).first()

            assert temp_user_query.username == user['username']
        return

    def test_user_info_nonexisting_user(self):
        nonexisting_user = "TestUser!"
        with self.app.app_context():
            users = db.session.query(User).all()
            for user in users:
                assert user.username != nonexisting_user

            response = self.client.post('/users/info', data=json.dumps(dict(username=nonexisting_user)),
                                        content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error == "User does not exist"
            assert result is False
        return

    def tearDown(self):
        return


if __name__ == '__main__':
    unittest.main()