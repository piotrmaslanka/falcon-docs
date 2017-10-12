# coding=UTF-8
from __future__ import print_function, absolute_import, division
import six
import inspect
import logging
import markdown2

logger = logging.getLogger(__name__)

MD = markdown2.Markdown()
convert = lambda o: inspect.getdoc(o) or u''

def method_to_body(method_name, method):
    return [u'<h2>Method %s</h2>' % (method_name, ), convert(method)]


def resource_to_body(resource):
    out = [u'<h1 id="r%s">Resource %s</h1>' % (resource.id, resource.main_name)]

    for url in resource.extra_urls:
        out.append(u'<div>Also known as <span style="font-weight: bold;">%s</span></div>' % (url, ))

    resource = resource.resource
    out.append(convert(resource))

    methods = ['post', 'put', 'get', 'patch', 'delete', 'options']

    for method in methods:
        if hasattr(resource, 'on_'+method):

            try:
                out.extend(method_to_body(method, getattr(resource, 'on_'+method)))
            except AttributeError as e:
                out.extend([u'<p style="font-style: italic;">No documentation provided for method %s<br>Detailed error: ' % (method, ),
                            str(e), u'</p>'])

    out.extend([u'<hr>'])
    return out
