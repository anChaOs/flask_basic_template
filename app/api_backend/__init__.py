#!/usr/bin/env python3
# coding: utf8
# 20170315 anChaOs

from flask import Blueprint

api_backend_blueprint = Blueprint('api_backend', __name__)

# this should at last
from . import views