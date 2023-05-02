<h1>Package canonical middleware Django</h1>

<p>Package canonical middleware Django permet d'introduire le variable lien canonical dans l'entête de réponse<p>
  
<p>Pour mettre en fonction cet élément vous devez ajoutez la ligne suivante dans votre setting django</p>

MIDDLEWARE = [
    'package-canonical-middleware-django.middleware.CanonicalMiddleware',
    ...
    ]
