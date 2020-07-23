#!/usr/bin/env python3
# coding: utf8
# 20170315 anChaOs

from flask import Blueprint

test_blueprint = Blueprint('test', __name__)

# this should at last
from . import views