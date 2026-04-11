import os
import sys

# Add your project parent folder to the Python path
sys.path.insert(0, '/home/earthsci/public_html/r/ESO2')

# Tell Django where your settings are
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ESO.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
