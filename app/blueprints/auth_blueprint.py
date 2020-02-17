import click
from flask import Blueprint, current_app

AuthBlueprint = Blueprint('AuthBlueprint', __name__)

@AuthBlueprint.route('/')
def hello():
  currentApp = current_app._get_current_object()

  return 'Auth Blueprint says hello!'