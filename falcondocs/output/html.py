# coding=UTF-8
from __future__ import print_function, absolute_import, division
import six
import logging
from .method import resource_to_body
logger = logging.getLogger(__name__)



def wrap(content, title=u'Documentation'):
   return b''.join(s.encode('utf8') for s in [u'''<!doctype HTML>
    <html lang="en">
    <head>
        <title>Documentation for %s</title>
        <meta charset="UTF-8">
    </head>
    <body>''' % (title, )] + content + [
       u'<hr><p style="font-size: small">Generated by falcondocs</p></body></html>'])


def process(resources):
    out = [u'<h1>Table of contents</h1><p style="margin-bottom: 30px;">']

    for res in resources.get_resources():
        out.extend([u'<a href="#r%s">%s</a><br>' % (res.id, res.main_name)])

    out.extend([u'</p><hr>'])

    for res in resources.get_resources():
        out.extend(resource_to_body(res))

    return out
