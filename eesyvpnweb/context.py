# -*- coding: utf-8 -*-


"""Context loaded and saved in WSGI requests"""


from webob.dec import wsgify


def make_add_context_to_request(app, app_ctx):
    """Return a WSGI middleware that adds context to requests."""
    @wsgify
    def add_context_to_request(req):
        req.ctx = app_ctx
        req.ctx.req = req
        return req.get_response(app)
    return add_context_to_request


class Context(object):
    _ = lambda self, message: message
    conf = None
    templates = None
