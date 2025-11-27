import os
class Config:
    SELECT_KEY = os.environment.get('SELECT_KEY') or ''
    
    #database config
    SQLALCHEMY_DATABASE_URL = 'sqlite://JobConnect.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False