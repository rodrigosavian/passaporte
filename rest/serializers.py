# -*- coding: utf-8 -*-
import json

from tornado.web import HTTPError


class Serializer(object):
    mapped_fields = None
    model_class = None

    def __init__(self, instance=None, body=None):
        self.instance = instance
        self.errors = {}

        if body:
            self.data_dict = self.build_data_dict(body)

    def build_data_dict(self, body):
        d = {}
        for k, v in body.items():
            try:
                field_model = self.mapped_fields[k]
            except KeyError, e:
                raise HTTPError(400)

            if isinstance(v, list):
                v = v.pop()
            d[k] = (field_model, v)
        return d

    def is_valid(self):
        for f in self.mapped_fields.keys():
            clean = getattr(self, 'clean_%s' % f, None)
            if callable(clean):
                clean()

        if self.errors:
            return False
        return True

    def set_error(self, field, error):
        self.errors[field] = error

    def save_model(self):
        self.instance.save()

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
