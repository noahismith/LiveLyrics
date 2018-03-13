import unittest
import json
from flask import make_response, redirect

import app
from app.models import User
from app import db

test_user = { "username": "TestUser",
              "spotify_id": "lnxd0zmjpsimn9mivdad7o9sh",
              "birthdate": "1990",
              "email": "invalidemail",
              "spotify_access_token": "BQBjIBJ2glAQhGjxKl38qesQR9K-hF05YQtWRMraJiwTflJci0ZO3XKGusOgij3A1Eq6gigvn1SDmKq_LYLhOWe1Lm59OPv1b3ma6pXldDwzE0MfCuyG0RSMsKRZFw1UNeENaBePRmYjcJja_KyquASs1FfG0GGj4Krpb3QBF0o5_7RMcUM",
              "spotify_refresh_token": "AQAF_XdbehzRIJ_8-vmmhcFaE7fc97ZZliBHjL6bNqv4zLiTzLJDVs2EGKCZ7eIJK16c0UVE8GpzuqY8_5h4aUYjLhnTK2gRg8HY9Z_uuuHu1Aoo6SFccPT72dPJYB26g3U"
}

class TestUsers(unittest.TestCase):

    def setUp(self):
        self.app = app.create_app("development")
        self.client = self.app.test_client(use_cookies=True)

        with self.app.app_context():
            db.create_all()


    def test_user_edit(self):
        with self.app.app_context():

            temp_user = db.session.query(User).filter_by(spotify_id=test_user["spotify_id"]).first()

            assert temp_user in db.session

            id = temp_user.id

            self.client.set_cookie("http://127.0.0.1:5000/", "access_token", test_user["spotify_access_token"])

            response = self.client.post('/users/edit', data=json.dumps(dict(username=test_user["username"],
                                                                             birthdate=test_user["birthdate"],
                                                                             email=test_user["email"])),
                                          content_type='application/json')
            print(response.get_data())

            temp_user = db.session.query(User).filter_by(id=id).first()

            assert temp_user.username == test_user["username"]
            assert temp_user.birthdate == test_user["birthdate"]
            assert temp_user.email == test_user["email"]

    def tearDown(self):
        return


if __name__ == '__main__':
    unittest.main()