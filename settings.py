# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine('mysql://root:@localhost/teste1', echo=False)
db = scoped_session(sessionmaker(bind=engine))
