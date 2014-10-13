# Django settings for munkiwebadmin project.
import os

USE_LDAP = False
# LDAP authentication support

LDAP_SETTINGS = {
    'base_dn': 'dc=central,dc=cmich,dc=local',
    'account_suffix': 'central.cmich.local',
    'servers': ['centraldc0%d.central.cmich.local' % i for i in xrange(1,2)],
    'staff_groups': ['aux-jradmins'],
    'superuser_groups': ['aux-admins','aux-jradmins']
}

AUTHENTICATION_BACKENDS = (
    #'django.contrib.auth.backends.ModelBackend',
    'techops.django_auth.backends.ActiveDirectoryBackend',
)

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Foo Bar', 'foo.bar@example.com'),
)

URL_BASE = "/apps/munkiwebadmin/"

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'munkiwebadmin',                      # Or path to database file if using sqlite3.
        'USER': 'munkiwebadmin',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '141.209.28.45',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Detroit'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"

#STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

STATIC_ROOT = '/apps/munkiwebadmin/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/apps/munkiwebadmin/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'site_static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'x@hgx4r!1rm@c4lax96tx88*d1v+m$&)w1ur4-xvcqj(8as_$q'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

LOGIN_URL='/apps/munkiwebadmin/login/'
LOGIN_REDIRECT_URL='/report/overview'

ROOT_URLCONF = 'munkiwebadmin.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'techops.django_auth',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    # Uncomment the next line if you've installed django_wsgiserver
    # and want to serve this Django app using it
    #'django_wsgiserver',
    'reports',
    'catalogs',
    'manifests',
    'inventory',
    'licenses',
    'gunicorn',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
     },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
	    'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

##############################
# MunkiWeb-specific settings #
##############################
# APPNAME is user-visable web app name
APPNAME = 'MunkiWebAdmin'
# MUNKI_REPO_DIR holds the local filesystem path to the Munki repo
MUNKI_REPO_DIR = ''

# provide the path to the git binary if you want MunkiWeb to add and commit
# manifest edits to a git repo
# if GITPATH is undefined or None MunkiWeb will not attempt to do a git add
# or commit
#GIT_PATH = '/usr/bin/git'

# name of the key in a manifest file that names the user or dept
MANIFEST_USERNAME_KEY = 'user'
# set MANIFEST_USERNAME_IS_EDITABLE to allow edits to the displayed username
MANIFEST_USERNAME_IS_EDITABLE = False

# enable WARRANTY to show warranty information on the detail machine report
WARRANTY_LOOKUP_ENABLED = False

# enable MODEL_LOOKUP_ENABLED to show a human readable version of the machines 
# model
MODEL_LOOKUP_ENABLED = False

# if MunkiWebAdmin is behind a proxy, and WARRANTY_LOOKUP_ENABLED or
# MODEL_LOOKUP_ENABLED are enabled, enter the details for the proxy server in
# the format user:password@example.com:port (user:password@ and :port are 
# optional), otherwise leave blank
PROXY_ADDRESS = ""
