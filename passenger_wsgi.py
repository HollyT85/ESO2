import os
import sys

sys.path.insert(0, '/home/earthsci/public_html/r/ESO2')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ESO.settings')

from ESO.wsgi import application as app
