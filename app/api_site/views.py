#!/usr/bin/env python3
# coding: utf8
# 20170315 anChaOs

# general
import json, time
import operator
import re

import requests  # for http requests
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
import config as config

# db
from app import db

# database functions
import app.database.api as dbapi

# error
import app.error as error

ApiError = error.ApiError

from app.tool import dbg  # for print
from app.tool import print_exception_info  # for traceback

# api
from .apis import *

# blueprint
from . import api_site_blueprint

# wrapper
from app.wrapper.wrapper import *


@api_site_blueprint.errorhandler(ApiError)
def handle_api_error(current_error):
    dbg((current_error.msg, current_error.error_no))
    # print_exception_info()
    error_info = error.get_error_info(current_error.error_no)
    return make_response(jsonify({'ret': current_error.error_no, 'msg': error_info[0]}), error_info[1])


@api_site_blueprint.errorhandler(Exception)
def handle_base_exception(current_error):
    print_exception_info()
    return make_response(json.dumps({'ret': 99, 'msg': 'server error'}), 500)


@api_site_blueprint.route('/<router>')
def site_fetch(router):
    dbg('site_fetch, %s' % router)
    reply, status_code = {'ret': 0, 'msg': ''}, 200

    if request.method == 'GET':
        try:
            router_list = list()
            assert (router in router_list)

            site_control = SiteControl(router.capitalize())

            params = request.args.to_dict()

            dbg(params)
        except:
            print_exception_info()
            raise ApiError('ERROR_PARAM', error.ERROR_PARAM)
        data = site_control.get_common(**params)

    if data is not None:
        reply['data'] = data

    return make_response(jsonify(reply), status_code)
