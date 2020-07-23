#!/usr/bin/env python3
# coding: utf8
# 20170220 anChaOs


# general
import json, time
import requests # for http requests
from datetime import datetime, timedelta, date

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
from app.database.api import dbapi

# error
import app.error as error

ApiError = error.ApiError

# normal functions
from .apis import *

from app.tool import dbg                    # for print
from app.tool import print_exception_info   # for traceback

import os, random, string


def wechat_login(code, state):
    if code and state:

        succ, res = wechatsdk.get_auth_user_info(appid, appsecret, code)
        try:
            if succ:
                dbg(res)
                openid = res['openid']
                access_token = res['access_token']

                user_auth = dbapi.UserAuth.get(identity_type='wechat', identifier=openid)
                if not user_auth:
                    # 1. 创建用户
                    user = dbapi.User.make_new()
                    db.session.flush()

                    # 2. 创建用户微信信息
                    kwargs = {
                        'user_id': user.id,
                        'openid': res['openid'],
                        'unionid': res.get('unionid', ''),
                        'nickname': res.get('nickname', ''),
                        'sex': res.get('sex', ''),
                        'province': res.get('province', ''),
                        'city': res.get('city', ''),
                        'country': res.get('country', ''),
                        'headimgurl': res.get('headimgurl', ''),
                        'privilege': json.dumps(res.get('privilege', '')),
                    }
                    wechat_user = dbapi.UserWechat.make_new(**kwargs)

                    # 3. 创建授权授权
                    identity_source = 1
                    identity_type = 'wechat'
                    identifier = openid
                    credential = access_token
                    user_auth = dbapi.UserAuth.make_new(user_id=user.id, 
                        identity_source=identity_source, identity_type=identity_type,
                        identifier=identifier, credential=credential)
                    db.session.commit()
                else:
                    user = dbapi.get_user(id=user_auth.user_id)

                next_url = state

                login_user(user)

                return redirect(next_url)
            else:
                dbg(str(res))
                return 'error'
        except:
            db.session.rollback()
            raise

    elif not code and not state:
        redirect_uri = config.REDIRECT_URI
        next_url     = request.args.get('next') or session.get('next_url') or 'http://'
        state        = next_url
        url          = wechatsdk.gen_auth_url(appid, redirect_uri, state)
        dbg('url: %s' % url)
        return redirect(url)


def web_login(username, password, remember_me):

    user_auth = dbapi.UserAuth.get(identity_source=0,
        identity_type='username', identifier=username)
    if not user_auth:
        raise ApiError('ERROR_NO_USER no user_auth', error.ERROR_NO_USER)

    if not user_auth.verify_password(password):
        raise ApiError('ERROR_WRONG_PSWD', error.ERROR_WRONG_PSWD)

    user = dbapi.User.get(id=user_aut.user_id)
    if not user:
        raise ApiError('ERROR_NO_USER no user', error.ERROR_NO_USER)

    user_roles = dbapi.UserRole.get(user_id=user.id)
    roles = [ user_role.role_id for user_role in user_roles ]

    login_user(user)

    if remember_me == 1:
        session.permanent = True
    elif remember_me == 0:
        session.permanent = False
    else:
        pass

    cur_authority = 'admin'

    data = {
        'name': user.name,
        'status': 'ok',
        'roles': roles,
    }

    return data


def get_cur_user():
    user_info = current_user.to_dict()
    user_roles = dbapi.UserRole.get(user_id=current_user.id)
    roles = [ user_role.role_id for user_role in user_roles ]
    user_info['roles'] = roles
    return user_info


def logout():
    logout_user()


def get_captcha(phone):

    reply_, status_code_ = openluat_api.verification_code(phone=phone)
    if status_code_ != requests.codes.ok:
        return make_response(jsonify(reply_), status_code_)


def reset_password(**kwargs):

    reply_, status_code_ = openluat_api.password(**kwargs)
    if status_code_ != requests.codes.ok:
        return make_response(jsonify(reply_), status_code_)


def register(**kwargs):

    kwargs['email'] = '%s@%s.com' % (kwargs['phone'], kwargs['phone'])
    reply_, status_code_ = openluat_api.register_user(**kwargs)
    if status_code_ != requests.codes.ok:
        return make_response(jsonify(reply_), status_code_)

    openluat_user_id = reply_['user_id']

    name = kwargs['username']
    index = random.randint(0, 7)
    avatar_url = DEFAULT_IMAGE[index]
    user = dbapi.User.make_new(openluat_user_id=openluat_user_id,
        name=name, avatar=avatar_url)
    db.session.flush()

    role_id = 1    # 普通用户
    user_role = dbapi.UserRole.make_new(user_id=user.id, role_id=role_id)
    db.session.commit()
