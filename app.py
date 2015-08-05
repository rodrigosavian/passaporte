# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web

from apps.people.apis.v1.api import PersonListAPI
from apps.people.apis.v1.api import PersonRetrieveAPI


application = tornado.web.Application([
    (r'/person$',  PersonListAPI),
    (r'/person/(\d+)$',  PersonRetrieveAPI),

])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
