import os
import sys
from django.conf import settings


# set DEBUG = True only if there's no other value coming to DEBUG from
# the environment variables
# to disable DEBUG you can now type e.g. $ export DEBUG=off
DEBUG = os.environ.get('DEBUG', 'on') == 'on'
# set a random new SECRET_KEY unless there's one coming from the environment
SECRET_KEY = os.environ.get('SECRET_KEY', '{{ secret_key }}')
# allows for comma-separated hostname input, defaults to localhost
# ALLOWED HOSTS verifies the HTTP request header values to check for matches
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

# building settings.py
settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


# Django settings need to be configured before other imports happen
# thus the uncommon double-import lines above and below here
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse


# building views.py
def index(request):
    return HttpResponse("get started building!")


# building urls.py
urlpatterns = [
    url(r'^$', index)
]


# create WSGI specs
application = get_wsgi_application()


# building manage.py
if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
