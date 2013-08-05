<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><%block name="title_content">EesyVPN</%block></title>
    <link rel="stylesheet" href="${helpers.relative_path(ctx, '/lib/bootstrap/2.2.2/css/bootstrap.min.css')}">
	<link rel="stylesheet" href="${helpers.relative_path(ctx, '/lib/bootstrap/2.2.2/css/bootstrap-responsive.css')}">
    <link rel="stylesheet" href="${helpers.relative_path(ctx, '/css/style.css')}">
  </head>
  <body>
    

<div class="navbar navbar-fixed-top">
  <div class="navbar-inner">
    <div class="container-fluid">
      <a class="brand" href="/">EesyVPN</a>
      <ul class="nav">
        <li class="dropdown">
			<a href="#" class="dropdown-toggle" data-toggle="dropdown">Certificates<b class="caret"></b></a>
			<ul class="dropdown-menu">
			  <li><a href="certs?state=valid&type=client">Clients</a></li>
			  <li><a href="certs?state=revoked">Revoked</a></li>
			  <li><a href="certs?type=server">Servers</a></li>
			</ul>
        </li>
      </ul>
    </div>
  </div>
</div>

    <div class="container-fluid content">
      
<%block name="body_content"/>

    </div>

    <!--[if lt IE 9]>
    <script src="${helpers.relative_path(ctx, '/lib/html5shiv/html5.js')}"></script>
    <![endif]-->
    <script src="${helpers.relative_path(ctx, '/lib/jquery/jquery-1.9.0.min.js')}"></script>
    <script src="${helpers.relative_path(ctx, '/lib/bootstrap/2.2.2/js/bootstrap.js')}"></script>
    
  </body>
</html>
