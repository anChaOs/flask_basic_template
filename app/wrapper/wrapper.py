#!/usr/bin/env python3
# coding: utf8
# 20170220 anChaOs

# wraps
from functools import wraps

# flask-login
from flask_login import login_user, logout_user, current_user
from flask_login import login_required, LoginManager

# database functions
from app.database.api import dbapi

# error
import app.error as error
ApiError = error.ApiError


def backend_required(func):
    @wraps(func)
    def wrapper(*args, **kw):
        user_roles = dbapi.UserRole.get(user_id=current_user.id)
        roles = [ user_role.role for user_role in user_roles ]
        if not roles:
            raise ApiError('ERROR_NO_USER no roles', error.ERROR_NO_USER)
        flag = False
        try:
            assert 0 in roles
        except:
            flag = True
        if flag:
            try:
                assert 1 in roles
            except:
                raise ApiError('ERROR_NO_USER not backend user', error.ERROR_NO_USER)
        return func(*args, **kw)
    return wrapper


def wechat_required(func):
    @wraps(func)
    def wrapper(*args, **kw):
        user_roles = dbapi.UserRole.get(user_id=current_user.id)
        roles = [ user_role.role for user_role in user_roles ]
        if 2 not in roles:
            raise ApiError('ERROR_NO_USER not wechat user', error.ERROR_NO_USER)
        return func(*args, **kw)
    return wrapper

