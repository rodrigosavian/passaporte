# -*- coding: utf-8 -*-
import json

from tornado.testing import AsyncHTTPTestCase

import app
from settings import db

from apps.people.models import Person


class PersonListAPITest(AsyncHTTPTestCase):
    model_class = Person

    def get_app(self):
        # first clear all
        db.query(self.model_class).delete()

        for x in range(5):
            p = self.model_class(
                    username=u'rodrigocesar.savian%s' % x,
                    facebook_id='100003194166055%s' % x,
                    name=u'Rodrigo Cesar Savian%s' % x,
                    gender=u'male')
            db.add(p)
        db.commit()
        self.object_list = db.query(self.model_class).all()
        self.object = self.object_list[0]
        return app.make_app_test()

    def test_status_code_person_list(self):
        response = self.fetch('/person/')
        self.assertEqual(response.code, 200)

    def test_without_limit_person_list(self):
        response = self.fetch('/person/')
        body = '{"limit": 5, "list": [{"username": "rodrigocesar.savian0", "facebookId": "1000031941660550", "name": "Rodrigo Cesar Savian0", "gender": "male"}, {"username": "rodrigocesar.savian1", "facebookId": "1000031941660551", "name": "Rodrigo Cesar Savian1", "gender": "male"}, {"username": "rodrigocesar.savian2", "facebookId": "1000031941660552", "name": "Rodrigo Cesar Savian2", "gender": "male"}, {"username": "rodrigocesar.savian3", "facebookId": "1000031941660553", "name": "Rodrigo Cesar Savian3", "gender": "male"}, {"username": "rodrigocesar.savian4", "facebookId": "1000031941660554", "name": "Rodrigo Cesar Savian4", "gender": "male"}]}'

        dict_object = json.loads(response.body)
        self.assertEqual(response.body, body)
        self.assertEqual(len(dict_object['list']), 5)

    def test_limit_two_person_list(self):
        response = self.fetch('/person/?limit=2')
        body = '{"limit": 5, "list": [{"username": "rodrigocesar.savian0", "facebookId": "1000031941660550", "name": "Rodrigo Cesar Savian0", "gender": "male"}, {"username": "rodrigocesar.savian1", "facebookId": "1000031941660551", "name": "Rodrigo Cesar Savian1", "gender": "male"}]}'

        dict_object = json.loads(response.body)
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, body)
        self.assertEqual(len(dict_object), 2)

    def test_create_person(self):
        response = self.fetch('/person/', method='POST', body='facebookId=100003194166055')
        self.assertEqual(response.code, 201)
