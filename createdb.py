# -*- coding: utf-8 -*-
from settings import engine

from rest.models import Model

from apps.people.models import Person


people_table = Person.__table__
metadata = Model.metadata

def create_all():
    metadata.create_all(engine)

if __name__ == '__main__':
    create_all()
