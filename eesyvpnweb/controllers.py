# -*- coding: utf-8 -*-


import logging

from webob.dec import wsgify

from . import conv, router, templates, wsgi_helpers

import eesyvpn


log = logging.getLogger(__name__)

@wsgify
def home(req):
    return templates.render(req.ctx, '/home.mako', data={})

@wsgify
def certs(req):
    params = req.params
    log.debug(u'params = {}'.format(params))
    inputs = {
        'type': params.get('type'),
        'state': params.get('state'),
        }
    log.debug(u'inputs = {}'.format(inputs))
    data, errors = conv.inputs_to_certs_data(inputs)
    if errors is not None:
        return wsgi_helpers.bad_request(req.ctx, comment=errors)
        
    log.debug(u'data = {}'.format(data))
    
    if data['type']=='client':
		if data['state']=='valid':
			data['certs']=eesyvpn.listValidCerts()
			return templates.render(req.ctx, '/certs_client_valid.mako', data=data)
    elif data['state']=='revoked':
		data['certs']=eesyvpn.listRevokedCerts()
		return templates.render(req.ctx, '/certs_client_revoked.mako', data=data)
    elif data['type']=='server':
		data['certs']=eesyvpn.listValidCerts(type='server')
		return templates.render(req.ctx, '/certs_server.mako', data=data)

@wsgify
def cert(req):
    params = req.params
    log.debug(u'params = {}'.format(params))
    inputs = {
        'id': params.get('id')
        }
    log.debug(u'inputs = {}'.format(inputs))
    data, errors = conv.inputs_to_cert_data(inputs)
    if errors is not None:
        return wsgi_helpers.bad_request(req.ctx, comment=errors)
        
    log.debug(u'data = {}'.format(data))
    
    data['name']=eesyvpn.nameById(data['id'])
    data['cert']=eesyvpn.view(data['id'])
    
    return templates.render(req.ctx, '/cert.mako', data=data)

def make_router():
    return router.make_router(
        ('GET', '^/$', home),
        ('GET', '^/certs$', certs),
        ('GET', '^/cert$', cert),
        )
