#!/usr/bin/env python3
# coding: utf8
# 20170220 anChaOs

from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__)

# this should at last
from . import views