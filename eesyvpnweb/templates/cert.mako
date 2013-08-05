## -*- coding: utf-8 -*-


<%inherit file="/site.mako"/>

<%block name="title_content">EesyVPN - Certificate ${data['name']}</%block>

<%block name="body_content"> 
<h1>Certificate ${data['name']}</h1>

% if 'error' in data:
<div class="alert alert-error">${data['error']}</div>
% endif

% if 'msg' in data:
<div class="alert alert-success">${data['msg']}</div>
% endif

% if 'cert' in data and data['cert']:
<pre>${data['cert']}</pre>
% endif
</%block>
