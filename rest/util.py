# -*- coding: utf-8 -*-
from tornado.web import HTTPError


def get_object_or_404(model_class, queryset, field, id):
    object = queryset.filter(getattr(model_class, field)==id).first()
    if object is None:
        raise HTTPError(404)
    return object
