from .service import Service

import sqlite3

from flask import current_app, g

class DBConnection(Service):
    """
    Service class for database connection.
    Extends the Service class.
    """
    def get_db(self) -> sqlite3.Connection:
        """
        Creates a database connection and stores it in the Flask application context.
        """
        if 'db' not in g:
            g.db = sqlite3.connect(
                current_app.config['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES
            )
            g.db.row_factory = sqlite3.Row

        return g.db


    def close_db(self, e=None):
        """
        Closes the database connection if it exists and removes it from the Flask application context.
        """
        db = g.pop('db', None)

        if db is not None:
            db.close()

    def init_db(self):
        """
        Initializes the database by creating the necessary tables.
        """

        db = self.get_db()

        with current_app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode('utf8'))

        
    def load_data(self):
        """
        Loads initial data into the database.
        """

        db = self.get_db()

        with current_app.open_resource('data.sql') as f:
            db.executescript(f.read().decode('utf8'))


