# -*- coding: utf-8 -*-
from sqlalchemy import (Column, Integer, String)

from rest.models import Model


class Person(Model):
    tablename = 'people'

    username = Column(String(30), nullable=True)
    facebook_id = Column(String(50), unique=True)
    name = Column(String(255), nullable=True)
    gender = Column(String(20), nullable=True)
