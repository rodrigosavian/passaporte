# -*- coding: utf-8 -*-
import json


class ListHandlerMixin(object):
    def list(self, *args, **kwargs):
        object_list = self.get_object_list()
        serializer = self.get_serializer(instance=object_list)
        self.write(json.dumps({'list': serializer.data, 'limit': self.count}))


class CreateHandlerMixin(object):
    def create(self, *args, **kwargs):
        serializer = self.get_serializer(body=self.request.arguments)
        response = ''
        if serializer.is_valid():
            serializer.save_model()
            status_code = 201
        else:
            response = serializer.errors
            status_code = 400

        self.write(json.dumps(response))
        self.set_status(status_code)
        self.set_header("Content-Type", "application/json")


class RetrieveHandlerMixin(object):
    def retrieve(self, id, *args, **kwargs):
        self.id = id
        object = self.get_object()
        serializer = self.get_serializer(instance=object)
        self.write(json.dumps(serializer.data))
