import os
import sys

sys.path.insert(0, '/home/earthsci/public_html/ESO')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ESO.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     return [b"HELLO FROM PASSENGER"]
