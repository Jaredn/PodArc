try:
    from settings import *
except ImportError:
    pass

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS += ("locations",)

print "INFO: This server is running with DEVELOPMENT-1 settings"
