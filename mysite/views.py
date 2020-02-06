from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    header = '''<!DOCTYPE html>
<html>
  <head>
    <title>django-cas-ng example demo</title>
    <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, minimum-scale=1.0">
  </head>
  <body>
  <h1>Welcome to django-cas-ng demo</h1>'''

    footer = '''<p>Related post:</p>
    <ul>
        <li><a href="https://djangocas.dev/blog/django-cas-ng-example-project/">Step by step to setup a django-cas-ng example project</a></li>
    </ul>
    <hr><p><a href="https://djangocas.dev/">Project homepage</a></p>
  </body>
</html>'''

    if request.user.is_authenticated:
        body = """
        <p>You logged in as <strong>%s</strong>.</p>
        <p><a href="/accounts/logout">Logout</a></p>
         """ % request.user.username
    else:
        body = '<p><a href="/accounts/login">Login</a></p>'

    return HttpResponse(header + body + footer)

def ping(request: HttpRequest) -> HttpResponse:
    return HttpResponse('pong', content_type="text/plain")
