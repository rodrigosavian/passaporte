# -*- coding: utf-8 -*-
from tornado.web import RequestHandler

from rest import mixins
from rest.util import get_object_or_404


class BaseRequestHandler(RequestHandler):

    model = None
    serializer_class = None

    def get_queryset(self):
        return self.model.query().filter()

    def get_object_list(self):
        return self.get_queryset().all()

    def get_object(self):
        queryset = self.get_queryset()
        return get_object_or_404(queryset, self.id)

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)


class ListRequestHandler(
        mixins.ListHandlerMixin,
        BaseRequestHandler):

    def get(self, *args, **kwargs):
        return self.list(*args, **kwargs)


class RetrieveRequestHandler(
        mixins.RetrieveHandlerMixin,
        BaseRequestHandler):

    def get(self, id, *args, **kwargs):
        return self.retrieve(id, *args, **kwargs)