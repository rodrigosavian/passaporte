# -*- coding: utf-8 -*-
from rest.serializers import Serializer


class PersonSerializer(Serializer):
    mapped_fields = {
        'facebookId': 'facebook_id',
        'username': 'username',
        'name': 'name',
        'gender': 'gender',
    }
