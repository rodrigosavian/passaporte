# -*- coding: utf-8 -*-
from sqlalchemy import (Column, Integer, String)
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import declarative_base

from settings import db


class Base(object):

    @declared_attr
    def __tablename__(cls):
        return cls.tablename or cls.__name__.lower()

    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return u'<%s (id:%s)>' % (type(self), self.id)

    def _get_fields(self):
        return dict((m.key, (m, getattr(self, m.key)))
                for m in self.__table__.columns)
    fields = property(_get_fields)

    def save(self, *args, **kwargs):
        if not self.id:
            db.add(self)
        db.commit()

    def delete(self, *args, **kwargs):
        try:
            db.delete(self)
            db.commit()
        except AttributeError, e:
            raise e
        else:
            return None

    @classmethod
    def query(cls):
        return db.query(cls)

Model = declarative_base(cls=Base)
