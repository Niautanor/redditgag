# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'super secret key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: in a production environment, you should add the fqdn of you
# server here
ALLOWED_HOSTS = []

# If you have SSL, you should probably set this to True
SECURE_SSL_REDIRECT = False

# Django's collectstatic command will put static files here. In a production
# environment, this should point to a directory that is served by your webserver
# under the STATIC_URL
STATIC_ROOT = None

# You might want to set this to True in a production environment if you don't
# want to / can't give the process that runs django access to your STATIC_ROOT
STATIC_PRECOMPILER_DISABLE_AUTO_COMPILE = False
