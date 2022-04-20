import sqlite3
from tkinter import E

import click
from flask import current_app, g
#current_app. g ? 뭘하는걸까. 
from flask.cli import with_appcontext

import psycopg2

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def get_db():
  print('getget_dbdb')
  if 'db' not in g:
    try:
      # g.db = sqlite3.connect(
      #     current_app.config['DATABASE'],
      #     detect_types=sqlite3.PARSE_DECLTYPES
      # )
      # g.db.row_factory = sqlite3.Row
      g.db = psycopg2.connect(
        #jdbc:postgresql://database-1.c8qyfxb7l3rj.ap-northeast-2.rds.amazonaws.com
      host="myfirstdbinstance.c8qyfxb7l3rj.ap-northeast-2.rds.amazonaws.com",
      database="firstdb",
      user="postgres123",
      password="rkdahdmlelql",
      port=5432)
    except Exception as e:
      print(f"error \n {e}")
      

  return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


###############################################################


def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')