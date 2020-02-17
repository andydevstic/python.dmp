import psycopg2
import click
from flask import current_app, g

class PgAdapter():
  def __init__(self, app):
    self.app = app

  def get_cursor(self):
    return self.cursor

  def connect_db(self):
    try:
      self.connection = psycopg2.connect(
        user = self.app.config['DB_USER'],
        password = self.app.config['DB_PASSWORD'],
        host = self.app.config['DB_HOST'],
        port = self.app.config['DB_PORT'],
        database = self.app.config['DB_NAME']
      )
      return self.connection
    except (Exception, psycopg2.Error) as Error:
      click.echo('Error while connecting to PostgreSQL')
      click.echo(Error)

  def close_db(self):
    if self.cursor is not None:
      self.cursor.close()


# cursor.execute('SELECT version();')
# record = cursor.fetchone()
# print("You are connected to - ", record,"\n")

'''
  We can create as many cursors as we want from a single connection object.
  Cursors created from the same connection are not isolated, i.e., any changes done to the database by a cursor are immediately visible by the other cursors.
  Cursors are not thread-safe
'''