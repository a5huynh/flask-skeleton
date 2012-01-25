'''
settings.py
    
Contains the settings for the Flask application. 
See http://flask.pocoo.org/docs/config/ for more details. 
'''
class Config( object ):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'CHANGE THIS!!!!!'
    CACHE_TYPE = 'simple'

class Dev( Config ):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../tmp/dev.db'

class Production( Config ):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../tmp/dev.db'
        
class Testing( Config ):
    TESTING = True