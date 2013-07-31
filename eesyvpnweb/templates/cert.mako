## -*- coding: utf-8 -*-


<%inherit file="/site.mako"/>

<%block name="title_content">EesyVPN - Certificate ${data['name']}</%block>

<%block name="body_content"> 
<h1>Certificate ${data['name']}</h1>

<pre>${data['cert']}</pre>
</%block>
