# -*- coding: utf-8 -*-
from tornado.web import HTTPError


def get_object_or_404(queryset, id):
    object = queryset.get(id)
    if object is None:
        raise HTTPError(404)
    return object
