from flask import Blueprint
routes = Blueprint('routes', __name__)

from .login import *
from .check_session import *
from .process_webm import *