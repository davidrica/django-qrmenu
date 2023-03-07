import os,sys

from django.core.wsgi import get_wsgi_application
sys.path.append('/home/webpython/qrmenu/')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qrmenu.settings')

application = get_wsgi_application()
