## -*- coding: utf-8 -*-


<%inherit file="/site.mako"/>

<%block name="title_content">EesyVPN - Clients certificates</%block>

<%block name="body_content">
<div class='row-fluid'>
	<div class='span9'><h1>Clients certificates</h1></div>
	<div class='span3 btn-title-right'><a class='btn btn-primary' href='cert?action=create'>Create new certificate</a></div>
</div>

<table class="table table-hover table-striped">
<tr>
	<th>Name</th>
	<th>Expiration date</th>
	<th>Actions</th>
</tr>
% for name in data['certs']:
<tr>
	<td><a href="cert?id=${data['certs'][name]['id']}">${name}</a></td>
	<td>${helpers.expire_date(data['certs'][name]['expire']) | n}</td>
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
