# -*- coding: utf-8 -*-
import json
import logging


logging.basicConfig(filename='passaporte.log',level=logging.INFO)


class ListHandlerMixin(object):
    def list(self, *args, **kwargs):
        object_list = self.get_object_list()
        serializer = self.get_serializer(instance=object_list)
        self.write(json.dumps({'list': serializer.data, 'limit': self.count}))
        logging.info(u'list people log')


class CreateHandlerMixin(object):
    def create(self, *args, **kwargs):
        serializer = self.get_serializer(body=self.request.arguments)
        response = ''
        if serializer.is_valid():
            serializer.save_model()
            status_code = 201
            logging.info(u'create person log')
        else:
            response = serializer.errors
            status_code = 400
            logging.info(u'create person errors log')

        self.write(json.dumps(response))
        self.set_status(status_code)


class RetrieveHandlerMixin(object):
    def retrieve(self, id, *args, **kwargs):
        self.id = id
        object = self.get_object()
        serializer = self.get_serializer(instance=object)
        self.write(json.dumps(serializer.data))
        logging.info(u'get person log')


class DestroyHandlerMixin(object):
    def destroy(self, id, *args, **kwargs):
        self.id = id
        object = self.get_object()
        serializer = self.get_serializer(instance=object)
        serializer.delete_model()
        self.set_status(204)
        self.write('')
        logging.info(u'destroy person log')
