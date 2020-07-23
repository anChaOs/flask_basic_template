#!/usr/bin/env python3
# coding: utf8
# 20170220 anChaOs


# general
import json, time
import requests # for http requests
from datetime import datetime, timedelta, date

# wraps
from functools import wraps

# flask
from flask import Flask, request, session, jsonify
from flask import redirect, url_for, render_template, make_response

# flask-login
from flask_login import login_user, logout_user, current_user
from flask_login import login_required, LoginManager

# config
from sqlalchemy import func

import config as config

# database functions
import app.database.api as dbapi

# error
import app.error as error
from .. import db

ApiError = error.ApiError

# normal functions
from .apis import *

from app.tool import dbg                    # for print
from app.tool import print_exception_info   # for traceback

# blueprint
from . import main_blueprint


@main_blueprint.errorhandler(ApiError)
def handle_api_error(current_error):
    dbg((current_error.msg, current_error.error_no))
    # print_exception_info()
    error_info = error.get_error_info(current_error.error_no)
    return make_response(jsonify({'ret':current_error.error_no, 'msg':error_info[0]}), error_info[1])


@main_blueprint.errorhandler(Exception)
def handle_base_exception(current_error):
    print_exception_info()
    return make_response(json.dumps({'ret':99, 'msg':'server error'}), 500)


@main_blueprint.route('/')
def index():
    dbg('index')
    reply ,status_code = {'ret': 0, 'msg': ''}, 200
    return make_response(jsonify(reply), status_code)

