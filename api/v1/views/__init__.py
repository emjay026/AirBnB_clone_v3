#!/usr/bin/python3
"""Package initializer"""

from flask import Blueprint
# Wildcard import everything in the package api.v1.views.index
from api.v1.views.index import *

# Create an instance of Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')