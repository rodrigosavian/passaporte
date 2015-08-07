# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web

from settings import cache

from apps.people.apis.v1.api import PersonListCreateAPI
from apps.people.apis.v1.api import PersonRetrieveDestroyAPI


class ConfigCreateAPI(tornado.web.RequestHandler):
    def post(self):
        for k, v in self.request.arguments.items():
            if isinstance(v, list):
                v = v.pop()
            cache.set(k, v)
        self.set_status(201)


application = tornado.web.Application([
    (r'/config/$', ConfigCreateAPI),
    (r'/person/$',  PersonListCreateAPI),
    (r'/person/(\d+)/$',  PersonRetrieveDestroyAPI),
])

def make_app_test():
    global application
    return application

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
