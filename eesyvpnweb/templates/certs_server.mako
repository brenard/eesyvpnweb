## -*- coding: utf-8 -*-


<%inherit file="/site.mako"/>

<%block name="title_content">EesyVPN - Servers certificates</%block>

<%block name="body_content"> 
<div class='row-fluid'>
	<div class='span9'><h1>Servers certificates</h1></div>
	<div class='span3 btn-title-right'><a class='btn btn-primary' href='cert?action=create&type=server'>Create new certificate</a></div>
</div>

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
