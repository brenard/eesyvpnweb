## -*- coding: utf-8 -*-


<%inherit file="/site.mako"/>

<%block name="title_content">EesyVPN - Servers certificates</%block>

<%block name="body_content"> 
<h1>Servers certificates</h1>

<table class="table table-hover table-striped">
<tr>
	<th>Name</th>
	<th>Expiration date</th>
</tr>
% for name in data['certs']:
<tr>
	<td><a href="cert?id=${data['certs'][name]['id']}">${name}</a></td>
	<td>${data['certs'][name]['expire']}</td>
</tr>
% endfor
</table>

</%block>
