# -*- coding: utf-8 -*-
from sqlalchemy import (Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    facebook_id = Column(String(50), nullable=False)
    name = Column(String(255), nullable=False)
    gender = Column(String(20), nullable=False)


    def __repr__(self):
        return u'<Person(%s)>' % self.facebook_id
