# -*- coding: utf-8 -*-
import json
import unittest

from settings import db

from apps.people.models import Person

from serializer import PersonSerializer


class PersonSerializerTest(unittest.TestCase):
    model_class = Person
    serializer_class = PersonSerializer

    def setUp(self):
        db.query(self.model_class).delete()
        db.commit()

        self.object_list = []
        for x in range(1, 5):
            p = self.model_class(
                    id=x,
                    username=u'rodrigocesar.savian%s' % x,
                    facebook_id='100003194166055%s' % x,
                    name=u'Rodrigo Cesar Savian%s' % x,
                    gender=u'male')
            self.object_list.append(p)
        self.object = self.object_list[0]
        self.serializer_object = self.serializer_class(self.object)

    def tearDown(self):
        db.query(self.model_class).delete()
        db.commit()

        del self.object
        del self.object_list

    def test_object_to_dict_method(self):
        object_dict = self.serializer_class.object_to_dict(self.object)
        self.assertEqual(object_dict, {
            'username': u'rodrigocesar.savian1',
            'facebookId': '1000031941660551',
            'name': u'Rodrigo Cesar Savian1',
            'gender': u'male'})

    def test_mapped_fields(self):
        self.assertEqual(self.serializer_object.mapped_fields, {
            'facebookId': 'facebook_id',
            'username': 'username',
            'name': 'name',
            'gender': 'gender'})

    def test_get_data_with_object(self):
        self.assertEqual(self.serializer_object.data, {
            'username': u'rodrigocesar.savian1',
            'facebookId': '1000031941660551',
            'name': u'Rodrigo Cesar Savian1',
            'gender': u'male'})

    def test_get_data_with_list(self):
        l = []
        for x in range(1, 5):
            l.append({
                'username': u'rodrigocesar.savian%s' % x,
                'facebookId': '100003194166055%s' % x,
                'name': u'Rodrigo Cesar Savian%s' % x,
                'gender': u'male'})

        serializer_list = self.serializer_class(self.object_list)
        self.assertEqual(serializer_list.data, l)

if __name__ == '__main__':
    unittest.main()
