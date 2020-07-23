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

# database functions
import app.database.api as dbapi
from app.database.model import *
ssn = dbapi.db.session

from app.tool import dbg                    # for print
from app.tool import print_exception_info   # for traceback

# blueprint
from . import test_blueprint


def test_required(func):
    @wraps(func)
    def wrappera(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrappera


@test_blueprint.route('/')
# @login_required
def index():
    return 'okok'


@test_blueprint.route('/page')
def page():
    return render_template('test.html')


@test_blueprint.route('/test', methods=["POST"])
def test():
    try:
        for k in request.form:
            print(k, request.form[k])
        reply ,status_code = {'ret': 0, 'msg': ''}, 200
        return make_response(jsonify(reply), status_code)
    except:
        print_exception_info()
        reply ,status_code = {'ret': 1, 'msg': 'error'}, 500
        return make_response(jsonify(reply), status_code)

@test_blueprint.route("/interface/api_site", methods=['GET'])
def api_site():

    return render_template("api_site.html")