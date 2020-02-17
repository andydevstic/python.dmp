from flask import Blueprint, g

ApiBlueprint = Blueprint('ApiBlueprint', __name__)

@ApiBlueprint.route('/')
def hello():
  db_cursor = g.db.cursor()
  db_cursor.execute("SELECT version();")
  data = db_cursor.fetchone()
  return 'Api blueprint says hello and data is: {}'.format(data)