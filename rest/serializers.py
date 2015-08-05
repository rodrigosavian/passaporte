# -*- coding: utf-8 -*-
import json


class Serializer(object):
    mapped_fields = None

    def __init__(self, instance):
        self.instance = instance

    def _get_data(self):
        if isinstance(self.instance, list):
            l = []
            for object in self.instance:
                l.append(type(self).object_to_dict(object))
            object = l
        else:
            object = type(self).object_to_dict(self.instance)

        return json.dumps(object)
    data = property(_get_data)

    @classmethod
    def object_to_dict(cls, object):
        d = {}
        for field, model_attr in cls.mapped_fields.items():
            try:
                d[field] = object.fields[model_attr][1]
            except KeyError, e:
                raise e
        return d
