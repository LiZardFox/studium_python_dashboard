import click
from study_dash.service import DBConnection, get_service_container

import sqlite3
from datetime import datetime


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    get_service_container().get_service(DBConnection).init_db()
    click.echo('Initialized the database.')


@click.command('load-data')
def load_data_command():
    """Clear the existing data and create new tables."""
    get_service_container().get_service(DBConnection).load_data()
    click.echo('Loaded example data into the database.')

sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)

def get_db():
    """Shorthand to retrieve the database connection."""
    return get_service_container().get_service(DBConnection).get_db()

def close_db(e=None):
    """Shorthand to close the database connection."""
    get_service_container().get_service(DBConnection).close_db()

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(load_data_command)