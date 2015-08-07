# -*- coding: utf-8 -*-
import redis

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine('mysql://root:@localhost/teste1', echo=False)
db = scoped_session(sessionmaker(bind=engine))

cache = redis.StrictRedis(host='localhost', port=6379, db=0)
