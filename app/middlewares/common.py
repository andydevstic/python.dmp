from flask import g

def register_db_connection(connection):
  def middleware():
    g.db = connection
  return middleware

def register_logger(logger):
  def middleware():
    g.logger = logger
  return middleware