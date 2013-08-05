## -*- coding: utf-8 -*-


<%inherit file="/site.mako"/>

<%block name="title_content">EesyVPN - Certificate ${data['name']}</%block>

<%block name="body_content"> 
<h1>Create new certificate</h1>

% if 'error' in data:
<div class="alert alert-error alert-block">${data['error'] | n}</div>
% endif

<form class="form-horizontal" action='cert'>
  <input type='hidden' name='action' value='create'/>
  <div class="control-group">
    <label class="control-label" for="name">Name</label>
    <div class="controls">
      <input type="text" id="name" name='name' placeholder="Name">
    </div>
  </div>
  <div class="control-group">
    <label class="control-label" for="tyoe">Type</label>
    <div class="controls">
      <select name='type'>
		<option value='client'>Client</option>
% if data['type']=='server':
		<option value='server' selected>Server</option>
% else:
		<option value='server'>Server</option>
% endif
      </select>
    </div>
  </div>
  <div class="control-group">
    <div class="controls">
      <button type="submit" class="btn">Create</button>
    </div>
  </div>
</form>

</%block>
