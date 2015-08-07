# -*- coding: utf-8 -*-
import tornado

from rest.handlers import ListCreateRequestHandler
from rest.handlers import RetrieveDestroyRequestHandler

from apps.people.models import *
from serializer import *


class PersonListCreateAPI(ListCreateRequestHandler):
    model = Person
    serializer_class = PersonSerializer


class PersonRetrieveDestroyAPI(RetrieveDestroyRequestHandler):
    model = Person
    serializer_class = PersonSerializer
    field_id = 'facebook_id'
