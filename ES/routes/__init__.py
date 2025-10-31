from flask import Blueprint

dp = Blueprint('main', __name__)

from . import routes_admin, routes_auth, routes_core, routes_project