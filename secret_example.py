# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'super secret key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: in a production environment, you should add the fqdn of you
# server here
ALLOWED_HOSTS = []

# If you have SSL, you should probably set this to True
SECURE_SSL_REDIRECT = False

# This sets a flag when sending the session cookie that prevents the users
# browser from sending the cookie over an unencrypted connection.
# Usually you would want this but the development server doesn't support https
SESSION_COOKIE_SECURE = False

# Django's collectstatic command will put static files here. In a production
# environment, this should point to a directory that is served by your webserver
# under the STATIC_URL
STATIC_ROOT = None

# You might want to set this to True in a production environment if you don't
# want to / can't give the process that runs django access to your STATIC_ROOT
STATIC_PRECOMPILER_DISABLE_AUTO_COMPILE = False

# To use the authentication functionality, you have to register an app with
# reddit (https://reddit.com/prefs/apps) and enter the necessary fields here
REDDIT_AUTH_CLIENT_ID = ''
REDDIT_AUTH_CLIENT_SECRET = ''
# useful for running a test server, in a production environment, you would
# replace http with htpps and localhost with your server name
REDDIT_AUTH_REDIRECT_URI = 'http://localhost:8000/auth_redirect'
