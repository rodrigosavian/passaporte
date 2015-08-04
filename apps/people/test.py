# -*- coding: utf-8 -*-
import unittest

from sqlalchemy import Column

from models import Person


class PersonModelTest(unittest.TestCase):
    def setUp(self):
        p = Person()
        p.id = 1
        p.username = 'rodrigosavian'
        p.facebook_id = '299389283'
        p.name = 'Rodrigo Savian'
        p.gender = 'male'
        self.person = p

    def test_field_names_model_person(self):
        fields = (
            'id',
            'username',
            'facebook_id',
            'name',
            'gender',
        )
        self.assertEqual(tuple(
                [x.key for x in self.person.__table__.columns]), fields)

    def test_struct_get_fields_method(self):
        get_fields = self.person._get_fields()
        self.assertEqual(type(get_fields), dict)
        for k, v in get_fields.items():
            column, value = v
            self.assertEqual(type(column), Column)
            self.assertEqual(value, getattr(self.person, k))

if __name__ == '__main__':
    unittest.main()
