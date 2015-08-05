# -*- coding: utf-8 -*-
class ListHandlerMixin(object):
    def list(self, *args, **kwargs):
        object_list = self.get_object_list()
        serializer = self.get_serializer(object_list)
        self.write(serializer.data)


class RetrieveHandlerMixin(object):
    def retrieve(self, id, *args, **kwargs):
        self.id = id
        object = self.get_object()
        serializer = self.get_serializer(object)
        self.write(serializer.data)
