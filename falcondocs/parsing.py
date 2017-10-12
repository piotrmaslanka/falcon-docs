# coding=UTF-8
from __future__ import print_function, absolute_import, division
import six
import logging
import collections

logger = logging.getLogger(__name__)

Resource = collections.namedtuple('Resource', ('resource', 'main_name', 'urls',
                                               'extra_urls', 'id',
                                               'method_map'))


class ResourceCollection(object):
    def __init__(self):
        self.resources = {}
        self.main_name = {}
        self.res_objs = set()
        self.method_maps = {}

    def get_resources(self):
        for res in self.res_objs:
            yield Resource(res, self.main_name[id(res)],
                           self.resources[id(res)],
                           self.get_extra_names(res),
                           id(res),
                           self.method_maps[id(res)])

    def add(self, url, resource, method_map):
        p = id(resource)
        if p in self.resources:
            self.resources[p].append(url)
        else:
            self.resources[p] = [url]
            self.main_name[p] = url
            self.method_maps[p] = method_map
        self.res_objs.add(resource)

    def get_main_name(self, res):
        return self.main_name[id(res)]

    def get_extra_names(self, res):
        return self.resources[id(res)][1:]
