import os
import sys

# Add project root to path
sys.path.insert(0, os.path.dirname(__file__))

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ESO.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()