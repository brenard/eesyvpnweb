## -*- coding: utf-8 -*-


<%inherit file="/site.mako"/>

<%block name="title_content">EesyVPN - Revoked certificates</%block>

<%block name="body_content"> 
<h1>Revoked certificates</h1>

<table class="table table-hover table-striped">
<tr>
	<th>Name</th>
	<th>Expiration date</th>
	<th>Revocation date</th>
	<th>Actions</th>
</tr>
% for name in data['certs']:
% for cert in data['certs'][name]:
<tr>
	<td><a href="cert?id=${cert['id']}">${name}</a></td>
	<td>${cert['expire']}</td>
	<td>${cert['revoke']}</td>
	<td>
		<a class='btn btn-warning' href='cert?action=recreate&name=${name}'><i class="icon-repeat icon-white"></i> Recreate</a>
	</td>
</tr>
% endfor
% endfor
</table>

</%block>
