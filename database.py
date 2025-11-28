import sqlite3
from datetime import datetime
from werkzeug.security import generate_password_hash

class Database:
    def __init__(self, db_name='JobConnect.db'):
        self.db_name = db_name
        self.init_database()

    def get_connection(self):
        """database connection"""
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Raw
        return conn
    
    