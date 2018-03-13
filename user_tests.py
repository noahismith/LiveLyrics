import unittest
import requests
import json
import os, sys
import datetime

import app
from app.models import User
from app import db


class TestUsers(unittest.TestCase):

    def setUp(self):
        self.app = app.create_app("development")
        self.client = self.app.test_client

        with self.app.app_context():
            db.create_all()

    def test_user(self):
        with self.app.app_context():
            temp_user = User("Test user", "lnxd0zmjpsimn9mivdad7o9sh", datetime.datetime.now(),
                             "test_user@gmail.com", "")
            temp_user.save()
            assert temp_user in db.session

            id = temp_user.id

            temp_user.username = "Edited username"
            temp_user.email = "editedemail@gmail.com"
            temp_user.save()

            temp_user = db.session.query(User).filter_by(id=id).first()

            assert temp_user.username == "Edited username"
            assert temp_user.email == "editedemail@gmail.com"

            temp_user.delete()
            assert temp_user not in db.session

    def tearDown(self):
        return


if __name__ == '__main__':
    unittest.main()