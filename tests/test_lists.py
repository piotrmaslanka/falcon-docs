# coding=UTF-8
from __future__ import print_function, absolute_import, division
import six
import logging
import falcon
from falcon import testing
from falcondocs import FalconDocumentationResource, FalconDocumentationRouter


class R(object):
    def on_get(self, req, resp):
        """
        Hello World!

        Parameters:
        * abba
        * beta
        """
        resp.status = falcon.HTTP_201

api = falcon.API(router=FalconDocumentationRouter())
FalconDocumentationResource(api).register(u'/docs')
api.add_route(u'/lol', R())


class TestWorks(testing.TestCase):
    def setUp(self):
        super(TestWorks, self).setUp()
        self.app = api

    def test_docs(self):
        resp = self.simulate_get(u'/docs')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(b'<ul>' in resp.content)
