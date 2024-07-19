from flask import Blueprint

bp = Blueprint('blueprint', __name__)

from app.blueprint import routes