import unittest
import json
from flask import make_response, redirect

import app
from app.models import User
from app import db

test_user = { "username": "TestUser",
              "spotify_id": "lnxd0zmjpsimn9mivdad7o9sh",
              "birthdate": "1990",
              "email": "steamaccount2012@gmail.com",
              "spotify_access_token": "BQCpoX9BeHL8QS5i73KAhVtCdJGljgcqQ34hJJieDsGoIsv7nPJRrzNe0fHw5DmeZj_I9IIwQcb-GKIcPw5AwiKks7AImHVKTB1ZWJMHiLD37LGsZ3MzKliVjCEh_nPH_qFTScMCgDg1Zi88teglZ5wD63lDPTIJSSiQVND_ekotutQq1fs",
              "spotify_refresh_token": "AQAhsXsAt99ehZp_4NXeijsUHWug8aotcqN7_cN-LZxoMzgw-MoQd_KWlAl7-juJcXu8wXA-w4FE4KA9k6grdDjlY9NPN_BqBxyjH1lzmcNCgLX17cwL75WqUf4UxdjJg4o"
}

class TestUsers(unittest.TestCase):

    def setUp(self):
        self.app = app.create_app("development")
        self.client = self.app.test_client(use_cookies=True)

        self.client.set_cookie("http://127.0.0.1:5000/", "access_token", test_user["spotify_access_token"])

        with self.app.app_context():
            db.create_all()

    def test_user_edit(self):
        with self.app.app_context():

            temp_user = db.session.query(User).filter_by(spotify_id=test_user["spotify_id"]).first()
            assert temp_user in db.session

            id = temp_user.id

            response = self.client.post('/users/edit', data=json.dumps(dict(username=test_user["username"],
                                                                             birthdate=test_user["birthdate"],
                                                                             email=test_user["email"])),
                                          content_type='application/json')

            resp = json.loads(response.data.decode())
            error = resp['error']
            result = resp['result']

            assert error == ""
            assert result is True

            temp_user = db.session.query(User).filter_by(id=id).first()

            assert temp_user.username == test_user["username"]
            assert temp_user.birthdate == test_user["birthdate"]
            assert temp_user.email == test_user["email"]

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
        return

    def test_user_edit_username_spaces(self):
        # TODO /users/edit call with username containing spaces
        # TODO: test for proper error code
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
        return

    def test_user_edit_duplicate(self):
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

            assert temp_user_query.toJSON() == user
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