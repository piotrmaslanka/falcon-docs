# coding=UTF-8
from __future__ import print_function, absolute_import, division

import logging

import falcon.routing

from .output import wrap, process
from .parsing import ResourceCollection

logger = logging.getLogger(__name__)


class FalconDocumentationRouter(falcon.routing.DefaultRouter):
    def __init__(self):
        super(FalconDocumentationRouter, self).__init__()
        self.resources = ResourceCollection()

    def add_route(self, uri_template, method_map, resource, *args, **kwargs):
        self.resources.add(uri_template, resource, method_map)
        super(FalconDocumentationRouter, self).add_route(uri_template,
                                                         method_map, resource,
                                                         *args, **kwargs)


class FalconDocumentationResource(object):
    def __init__(self, api):
        self.api = api

    def register(self, base_url='/docs'):
        self.api.add_route(base_url, self)
        self.api.add_sink(self, prefix=base_url)

    def on_get(self, req, resp):
        out = process(self.api._router.resources, self)
        resp.content_type = 'text/html; charset=utf-8'
        resp.status = falcon.HTTP_200
        resp.data = wrap(out)
