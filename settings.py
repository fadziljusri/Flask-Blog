import os

SECRET_KEY = 'superdupersecrethere'
DEBUG = True
DB_USERNAME = 'root'
DB_PASSWORD = 'aaaa'
DB_NAME = 'blog'
DB_HOST = 'mysql:3306'
# DB_HOST = 'os.getenv('IP','0.0.0.0')'
# DB_PORT = int(os.getenv('PORT', 5000))
DB_URI = 'mysql+pymysql://%s:%s@%s/%s' % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
UPLOADED_IMAGES_DEST = '/opt/flask_blog/static/images/'
UPLOADED_IMAGES_URL = '/static/images/'