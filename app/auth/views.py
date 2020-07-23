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

# db
from app import db

# config
import config as config

# database functions
from app.database import User
from app.database.api import dbapi

# error
import app.error as error
ApiError = error.ApiError

# normal functions
from .apis import *

from app.tool import dbg                    # for print
from app.tool import print_exception_info   # for traceback

# blueprint
from . import auth_blueprint


@auth_blueprint.errorhandler(ApiError)
def handle_api_error(current_error):
    dbg((current_error.msg, current_error.error_no))
    error_info = error.get_error_info(current_error.error_no)
    return make_response(jsonify({'ret':current_error.error_no, 'msg':error_info[0]}), error_info[1])


@auth_blueprint.errorhandler(Exception)
def handle_base_exception(current_error):
    print_exception_info()
    return make_response(json.dumps({'ret':99, 'msg':'server error'}), 500)


@auth_blueprint.route('/unlogin')
def unlogin():
    dbg('unlogin')
    reply ,status_code = {'ret': 0, 'msg': ''}, 200
    # if config.API_WECHAT_PREFIX in request.args.get('next'):
    #     session['next_url'] = request.url
    #     return redirect(url_for('auth.wechat_login'))
    # else:
        # raise ApiError('unlogin', error.ERROR_NO_LOGIN)

    raise ApiError('unlogin', error.ERROR_NO_LOGIN)

    return make_response(jsonify(reply), status_code)


@auth_blueprint.route('/wechat/login')
def wechat_login():
    dbg('wechat_login')
    code  = request.args.get('code')
    state = request.args.get('state')

    appid       = config.APPID
    appsecret   = config.APPSECRET

    dbg((appid, appsecret))

    return auth_core.wechat_login(code, state)


@auth_blueprint.route('/login', methods=['POST'])
def login():
    dbg('login')
    reply ,status_code = {'ret': 0, 'msg': ''}, 200

    if request.method == 'POST':

        try:
            data = request.get_json()
            username = data['username']
            password = data['password']
        except:
            print_exception_info()
            raise ApiError('ERROR_PARAM', error.ERROR_PARAM)

        remember_me = 0
        try:
            remember_me = data['remember_me']
        except:
            pass

    data = auth_core.web_login(username, password, remember_me)

    if data:
        if isinstance(data, dict):
            reply['data'] = data
        else:
            return data

    return make_response(jsonify(reply), status_code)


@auth_blueprint.route('/cur')
@login_required
def get_cur_user():
    dbg('get_cur_user')
    reply ,status_code = {'ret': 0, 'msg': ''}, 200

    if request.method == 'GET':

        data = auth_core.get_cur_user()

        if data:
            reply['data'] = data

    return make_response(jsonify(reply), status_code)


@auth_blueprint.route('/logout', methods=['POST'])
@login_required
def logout():
    dbg('logout')
    reply ,status_code = {'ret': 0, 'msg': ''}, 200

    if request.method == 'POST':

        auth_core.logout()

    return make_response(jsonify(reply), status_code)


@auth_blueprint.route('/captcha', methods=['POST'])
def captcha():
    dbg('captcha')
    reply ,status_code = {'ret': 0, 'msg': ''}, 200

    if request.method == 'POST':
        try:
            data = request.get_json()
            phone = data['phone']
        except:
            print_exception_info()
            raise ApiError('ERROR_PARAM', error.ERROR_PARAM)

        data = auth_core.get_captcha(phone)
        if data:
            if isinstance(data, dict):
                reply['data'] = data
            else:
                return data

    return make_response(jsonify(reply), status_code)


@auth_blueprint.route('/reset_password', methods=['POST'])
def reset_password():
    dbg('reset_password')
    reply ,status_code = {'ret': 0, 'msg': ''}, 200

    if request.method == 'POST':
        try:
            data = request.get_json()
            phone    = data['phone']
            password = data['new_password']
            code     = data['code']
        except:
            print_exception_info()
            raise ApiError('ERROR_PARAM', error.ERROR_PARAM)

        data = auth_core.reset_password(**data)
        if data:
            if isinstance(data, dict):
                reply['data'] = data
            else:
                return data

    return make_response(jsonify(reply), status_code)


@auth_blueprint.route('/register', methods=['POST'])
def register():
    dbg('register')
    reply ,status_code = {'ret': 0, 'msg': ''}, 200

    if request.method == 'POST':

        try:
            data = request.get_json()
            username = data['username']
            phone    = data['phone']
            password = data['password']
            code     = data['code']
            dbg(data)
        except:
            print_exception_info()
            raise ApiError('ERROR_PARAM', error.ERROR_PARAM)

        data = auth_core.register(**data)
        if data:
            if isinstance(data, dict):
                reply['data'] = data
            else:
                return data

    return make_response(jsonify(reply), status_code)
