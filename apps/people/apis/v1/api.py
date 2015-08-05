# -*- coding: utf-8 -*-
import tornado

from rest.handlers import ListRequestHandler
from rest.handlers import RetrieveRequestHandler

from apps.people.models import *
from serializer import *


class PersonListAPI(ListRequestHandler):
    model = Person
    serializer_class = PersonSerializer


class PersonRetrieveAPI(RetrieveRequestHandler):
    model = Person
    serializer_class = PersonSerializer
