# -*- coding: utf-8 -*-
import unittest

from models import Person


class PersonModelTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_field_names_model_person(self):
        fields = (
            'id',
            'username',
            'facebook_id',
            'name',
            'gender',
        )
        self.assertEqual(
                tuple([x.key for x in Person.__table__.columns]), fields)

if __name__ == '__main__':
    unittest.main()
