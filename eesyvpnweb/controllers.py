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
		return templates.render(req.ctx, '/certs_revoked.mako', data=data)
	elif data['type']=='server':
		data['certs']=eesyvpn.listValidCerts(type='server')
		return templates.render(req.ctx, '/certs_server.mako', data=data)

@wsgify
def cert(req):
	params = req.params
	log.debug(u'params = {}'.format(params))
	inputs = {
		'id': params.get('id'),
		'action': params.get('action'),
		'name': params.get('name'),
		'type': params.get('type'),
		}
	log.debug(u'inputs = {}'.format(inputs))
	data, errors = conv.inputs_to_cert_data(inputs)
	if errors is not None:
		return wsgi_helpers.bad_request(req.ctx, comment=errors)

	if data['action']=='create':
		if data['name'] is None:
			return templates.render(req.ctx, '/cert_create.mako', data=data)
		else:
			if data['type']=='server':
				typ='server'
			else:
				typ='client'
			try:
				if eesyvpn.create(data['name'],type=typ):
					data['msg']="Certificate %s successfuly created !" % data['name']
					data['cert']=eesyvpn.view(data['name'])
				else:
					data['error']="Error creating certificate %s" % data['name']
					return templates.render(req.ctx, '/cert_create.mako', data=data)
			except Exception, e:
				data['error']="<h4>Error creating certificate %s :</h4>\n<pre>%s</pre>" % (data['name'],e)
				return templates.render(req.ctx, '/cert_create.mako', data=data)
	elif data['action'] and data['name']:
		log.debug('Run action "%s" on %s certificate' % (data['action'],data['name']))
		if data['action']=='renew':
			log.debug('Renew %s certificate' % data['name'])
			if eesyvpn.renew(data['name']):
				data['msg']="Certificate %s successfuly renewed !" % data['name']
			else:
				data['error']="Error renewing certificate %s." % data['name']
		elif data['action']=='recreate':
			log.debug('Recreate %s certificate' % data['name'])
			if eesyvpn.recreate(data['name']):
				data['msg']="Certificate %s successfuly recreate !" % data['name']
			else:
				data['error']="Error recreating certificate %s." % data['name']
		elif data['action']=='revoke':
			log.debug('Revoke %s certificate' % data['name'])
			if eesyvpn.revoke(data['name']):
				data['msg']="Certificate %s successfuly revoke !" % data['name']
			else:
				data['error']="Error revoking certificate %s." % data['name']
		data['cert']=eesyvpn.view(data['name'])
	elif data['id'] is not None:
		log.debug('Display template %s' % data['name'])
		data['name']=eesyvpn.nameById(data['id'])
		data['cert']=eesyvpn.view(data['id'])
	else:
		return wsgi_helpers.bad_request(req.ctx, comment='Missing parameter')
	log.debug(u'Template data = {}'.format(data))
	return templates.render(req.ctx, '/cert.mako', data=data)

def make_router():
	return router.make_router(
		('GET', '^/$', home),
		('GET', '^/certs$', certs),
		('GET', '^/cert$', cert),
		)
