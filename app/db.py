import sqlite3
import click

from flask import current_app, g

"""

Return a connection with our database. Creates one if it isn't in the current shared context variable, g

"""
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row

    return g.db

"""

Close an existing database connection

"""
def close_db(e = None):
    db = g.pop("db", None)

    if db is not None:
        db.close()

"""

Initialize the database with our schema

"""
def init_db():
    db = get_db()

    with current_app.open_resource("schema.sql") as f: 
        db.executescript(f.read().decode("utf-8"))

@click.command('init-db')
def init_db_command():
    init_db()
    click.echo("Initialized the Database.")

"""

register our database so that the connection is closed on request context pop
register our click command so we can initialize the databse outside of an app instance

"""
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)