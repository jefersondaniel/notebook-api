import os

# ***********************************
# Settings common to all environments
# ***********************************

# Application settings
APP_NAME = "AppName"
APP_SYSTEM_ERROR_SUBJECT_LINE = APP_NAME + " system error"

# Flask settings
CSRF_ENABLED = False
JSONIFY_PRETTYPRINT_REGULAR = False
DEBUG = bool(os.environ.get('DEBUG', False))


# *****************************
# Environment specific settings
# *****************************

# PLEASE USE A DIFFERENT KEY FOR PRODUCTION ENVIRONMENTS!
# Flask settings                    # Generated with: import os; os.urandom(24)
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    '\xb8\xaeu\xa5K\x8e\xf9\x9bW\x8d\xb4\xdb\xaf\xd1:\x89\xd5\xc3n\x19^},&'
)
DATABASE_HOST = os.environ.get('DATABASE_HOST', 'localhost')
DATABASE_PORT = int(os.environ.get('DATABASE_PORT', '27017'))
DATABASE_USER = os.environ.get('DATABASE_USER', None)
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', None)
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'notebook_test')
