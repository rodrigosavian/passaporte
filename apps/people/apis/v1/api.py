# -*- coding: utf-8 -*-
import tornado

from rest.handlers import ListCreateRequestHandler
from rest.handlers import RetrieveRequestHandler

from apps.people.models import *
from serializer import *


class PersonListAPI(ListCreateRequestHandler):
    model = Person
    serializer_class = PersonSerializer


class PersonRetrieveAPI(RetrieveRequestHandler):
    model = Person
    serializer_class = PersonSerializer
    field_id = 'facebook_id'
