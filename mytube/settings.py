from dotenv import load_dotenv

from os import environ

load_dotenv()


# Flask
STATIC_DIR = environ.get('STATIC_DIR', 'static/')
SECRET_KEY = environ.get('SECRET_KEY', 'a-very-bad-secret-key-please-use-something-else')


# Flask-Session
FLASK_SESSION_TYPE = environ.get('FLASK_SESSION_TYPE', 'filesystem')


# Flask and SQLAlchemy
SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)
SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///mytube.sqlite3')
FLASK_ADMIN_NAME = environ.get('FLASK_ADMIN_NAME', 'MyTube Admin')
FLASK_ADMIN_TEMPLATE_MODE = environ.get('FLASK_ADMIN_TEMPLATE_MODE', 'bootstrap3')


# Flask-Uploads
UPLOADS_DEFAULT_DEST = environ.get('UPLOADS_DEFAULT_DEST', 'mytube/static/')
ALLOWED_UPLOAD_TYPES = environ.get('UPLOADED_FILES_ALLOW', 'mp4,m4v,flv')  # comma-separated values


# Auth
AUTH_NAME = environ.get('AUTH_NAME', 'auth0')
AUTH_CLIENT_ID = environ['AUTH_CLIENT_ID']
AUTH_CLIENT_SECRET = environ['AUTH_CLIENT_SECRET']
AUTH_API_BASE_URL = environ['AUTH_API_BASE_URL']
AUTH_ACCESS_TOKEN_URL = environ['AUTH_ACCESS_TOKEN_URL']
AUTH_AUTHORIZE_URL = environ['AUTH_AUTHORIZE_URL']
AUTH_CALLBACK_URL = environ.get('AUTH_CALLBACK_URL', 'http://localhost:5000/auth/callback')
AUTH_LOGOUT_URL = environ['AUTH_LOGOUT_URL']
