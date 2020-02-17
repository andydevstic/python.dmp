import os
import click
from flask import Flask, g, request
from core.db import PgAdapter
from middlewares import register_db_connection, register_logger
from flask_dotenv import DotEnv
from blueprints import AuthBlueprint, ApiBlueprint

class Server:
  def __init__(self):
    self.app = Flask(__name__)
    self.init_env()
    self.init_neccessary_dirs()
    self.init_db()
    self.init_middlewares()
    self.init_blueprints()

  def init_env(self):
    DotEnv(self.app)

  def get_app(self):
    return self.app

  def init_blueprints(self):
    self.app.register_blueprint(AuthBlueprint, url_prefix='/auth')
    self.app.register_blueprint(ApiBlueprint, url_prefix='/api')

  def init_middlewares(self):
    self.app.before_request(register_db_connection(self.db_connection))
    self.app.before_request(register_logger(self.app.logger))

  def init_neccessary_dirs(self):
    try:
      if (os.path.exists(self.app.instance_path) == False):
        os.makedirs(self.app.instance_path)
    except OSError:
      click.echo("Can't create instance_path")

  def init_db(self):
    db_adapter = PgAdapter(self.app)
    self.db_connection = db_adapter.connect_db()

if __name__ == '__main__':
  app = Flask(__name__)
  app.run(debug=True)