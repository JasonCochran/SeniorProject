import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

basedir = os.path.abspath(os.path.dirname(__file__))

username = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASS']
db       = os.environ['POSTGRES_DBNAME']
port     = os.environ['POSTGRES_PORT']

SQLALCHEMY_DATABASE_URI = 'postgresql://' + username + ':' + password + '@postGIS:' + port + '/' + db
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
