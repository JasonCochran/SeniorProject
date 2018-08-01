import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql://root:1234@127.0.0.1:3306/kraken_ingest'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
