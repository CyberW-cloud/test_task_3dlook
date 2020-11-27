import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_task_3dlook.settings.development')

application = get_wsgi_application()
