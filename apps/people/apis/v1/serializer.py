# -*- coding: utf-8 -*-
import requests

from rest.serializers import Serializer

from apps.people.models import Person
from apps.people.util import facebook_request


class PersonSerializer(Serializer):
    facebook_api_url = 'https://graph.facebook.com/%s'
    mapped_fields = {
        'facebookId': 'facebook_id',
        'username': 'username',
        'name': 'name',
        'gender': 'gender',
    }
    model_class = Person

    def clean_facebookId(self):
        try:
            facebook_id = self.data_dict.get('facebookId')[1]
        except:
            return self.set_error('facebookId', u'facebookId required.')

        object = self.model_class.query().filter(
                self.model_class.facebook_id==facebook_id).first()

        # Test unique
        if object:
            return self.set_error('facebookId', u'facebookId already exists.')

        r = facebook_request(facebook_id)

        if r.status_code != 200:
            return self.set_error('facebookId', u'facebookId does not exist.')

    def save_model(self):
        facebook_id = self.data_dict.get('facebookId')[1]
        r = facebook_request(facebook_id)
        facebook_object = r.json()
        object = self.model_class()
        object.facebook_id = facebook_id
        object.username = facebook_object.get('first_name')
        object.name = facebook_object.get('name')
        object.gender = facebook_object.get('gender')
        object.save()
