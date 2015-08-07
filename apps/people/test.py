# -*- coding: utf-8 -*-
import unittest

from sqlalchemy import Column
from sqlalchemy.orm.query import Query

from settings import db

from models import Person


class PersonModelTest(unittest.TestCase):
    model_class = Person

    def setUp(self):
        db.query(self.model_class).delete()
        db.commit()

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

    def tearDown(self):
        db.query(self.model_class).delete()
        db.commit()
        del self.object
        del self.object_list

    def test_field_names_model_person(self):
        fields = (
            'id',
            'username',
            'facebook_id',
            'name',
            'gender',
        )
        self.assertEqual(tuple(
                [x.key for x in self.object.__table__.columns]), fields)

    def test_struct_get_fields_method(self):
        get_fields = self.object._get_fields()
        self.assertEqual(type(get_fields), dict)
        for k, v in get_fields.items():
            column, value = v
            self.assertEqual(type(column), Column)
            self.assertEqual(value, getattr(self.object, k))

    def test_return_objects_method(self):
        self.assertEqual(type(self.model_class.query()), Query)

    def test_create_person(self):
        p = self.model_class(
                username='rodrigosavian',
                facebook_id='29938992',
                name=u'Rodrigo Savian',
                gender=u'male')
        p.save()
        self.assertTrue(p.id)

    def test_update_person(self):
        self.object.username = 'rafaelc'
        self.object.facebook_id = '2999389'
        self.object.name = u'Rafael Castro'
        self.object.gender = u'male'
        self.object.save()

        person = self.model_class.query().get(self.object.id)
        self.assertEqual(person.username, self.object.username)
        self.assertEqual(person.facebook_id, self.object.facebook_id)
        self.assertEqual(person.name, self.object.name)
        self.assertEqual(person.gender, self.object.gender)

    def test_delete_person(self):
        self.assertEqual(self.object.delete(), None)

if __name__ == '__main__':
    unittest.main()
