#!/usr/bin/env python3
# coding: utf8
# 20170315 anChaOs

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
from sqlalchemy import not_

import config as config

# db
from app import db

# database functions
import app.database.api as dbapi

# core
from app.core.backend_core import *

# error
import app.error as error

ApiError = error.ApiError

from app.tool import dbg                    # for print
from app.tool import print_exception_info   # for traceback

# blueprint
from . import api_backend_blueprint

# wrapper
from app.wrapper.wrapper import *


@api_backend_blueprint.errorhandler(ApiError)
def handle_api_error(current_error):
    dbg((current_error.msg, current_error.error_no))
    # print_exception_info()
    error_info = error.get_error_info(current_error.error_no)
    return make_response(jsonify({'ret':current_error.error_no, 'msg':error_info[0]}), error_info[1])


@api_backend_blueprint.errorhandler(Exception)
def handle_base_exception(current_error):
    print_exception_info()
    return make_response(json.dumps({'ret':99, 'msg':'server error'}), 500)


@api_backend_blueprint.route('/user', methods=["GET", "PUT"])
@login_required
def user():
    dbg('user')
    reply ,status_code = {'ret': 0, 'msg': ''}, 200

    backend_user_control = BackendUserControl()

    if request.method == 'GET':
        params = request.args.to_dict()
        dbg(params)
        data = backend_user_control.get_user(**params)

    elif request.method == 'POST':
        # 暂不支持新增用户
        pass

    elif request.method == 'PUT':
        try:
            kwargs = request.get_json()
            dbg(kwargs)
            obj_id = kwargs['obj_id']
            update = kwargs['update']
            keys = ('banned', 'roles', 'name')
            for key in update:
                assert(key in keys)
        except:
            print_exception_info()
            raise ApiError('ERROR_PARAM', error.ERROR_PARAM)

        data = backend_user_control.update_user(obj_id, update)

    elif request.method == 'DELETE':
        # 暂不支持删除用户
        pass

    if data is not None:
        reply['data'] = data

    return make_response(jsonify(reply), status_code)

