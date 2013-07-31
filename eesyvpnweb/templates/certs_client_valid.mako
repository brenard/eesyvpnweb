## -*- coding: utf-8 -*-


<%inherit file="/site.mako"/>

<%block name="title_content">EesyVPN - Clients certificates</%block>

<%block name="body_content"> 
<h1>Clients certificates</h1>

<table class="table table-hover table-striped">
<tr>
	<th>Name</th>
	<th>Expiration date</th>
	<th>Actions</th>
</tr>
% for name in data['certs']:
<tr>
	<td><a href="cert?id=${data['certs'][name]['id']}">${name}</a></td>
	<td>${data['certs'][name]['expire']}</td>
	<td>
		<a class='btn btn-primary' href='cert?action=renew&name=${name}'><i class="icon-refresh icon-white"></i> Renew</a>
		<a class='btn btn-warning' href='cert?action=recreate&name=${name}'><i class="icon-repeat icon-white"></i> Recreate</a>
		<a class='btn btn-danger' href='cert?action=revoke&name=${name}'><i class="icon-ban-circle icon-white"></i> Revoke</a>
		<a class='btn btn-info' href='cert?action=download&name=${name}'><i class="icon-download icon-white"></i> Download</a>
	</td>
</tr>
% endfor
</table>

</%block>
