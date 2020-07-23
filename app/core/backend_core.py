#!/usr/bin/env python3
# coding: utf8
# 20170220 anChaOs


# general
import os, json, time, random, string
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


class BackendControl(object):

    def __init__(self, model_name):
        self.db_handler = getattr(dbapi, model_name)

    def _obj_to_dict(self, obj):
        # 子类可能需要重写该方法
        info = obj.to_dict()
        return info

    def get_common(self, **kwargs):
        result = self.db_handler.get(**kwargs)
        if result is None:
            raise ApiError('ERROR_NO_TARGET', error.ERROR_NO_TARGET)

        if isinstance(result, tuple):
            # 分页数据
            data = []
            count, items = result
            if count:
                for item in items:
                    info = self._obj_to_dict(item)
                    data.append(info)
            return {'count': count, 'items': data}

        elif isinstance(result, list):
            # 多条数据
            return list( self._obj_to_dict(item) for item in result )

        else:
            # 单条数据
            return self._obj_to_dict(result)

    def add_common(self, **kwargs):
        try:
            self.db_handler.make_new(**kwargs)
            db.session.commit()
        except:
            db.session.rollback()
            raise

    def update_common(self, obj_id, update):
        obj = self.db_handler.get(id=obj_id)
        if not obj:
            raise ApiError('ERROR_NO_TARGET', error.ERROR_NO_TARGET)
        try:
            self.db_handler.update(obj, **update)
            db.session.commit()
        except:
            db.session.rollback()
            raise

    def deleted_common(self, obj_id):
        obj = self.db_handler.get(id=obj_id)
        if not obj:
            raise ApiError('ERROR_NO_TARGET', error.ERROR_NO_TARGET)
        try:
            self.db_handler.update(obj, deleted=1)
            db.session.commit()
        except:
            db.session.rollback()
            raise


class BackendUserControl(BackendControl):

    def __init__(self):
        self.db_handler = dbapi.User
        self.db_user_role_handle = dbapi.UserRole

    def _obj_to_dict(self, obj):
        info = obj.to_dict()
        # roles
        user_roles = self.db_user_role_handle.get(user_id=obj.id) or []
        roles = [ user_role.role for user_role in user_roles ]
        if not roles:
            roles = []
        info['roles'] = roles
        return info

    def get_user(self, **kwargs):
        result = self.db_handler.get(**kwargs)
        if result is None:
            raise ApiError('ERROR_NO_USER', error.ERROR_NO_USER)

        if isinstance(result, tuple):
            # 分页数据
            data = []
            count, items = result
            if count:
                for item in items:
                    info = self._obj_to_dict(item)
                    data.append(info)
            return {'count': count, 'items': data}

        elif isinstance(result, list):
            # 多条数据
            return list( self._obj_to_dict(item) for item in result )

        else:
            # 单条数据
            return self._obj_to_dict(result)

    def update_user(self, obj_id, update):
        user = self.db_handler.get(id=obj_id)
        if not user:
            raise ApiError('ERROR_NO_USER', error.ERROR_NO_USER)
        try:
            # roles
            if 'roles' in update:
                roles = update.pop('roles')
                # 删除旧的权限
                self.db_user_role_handle.delete_user_roles(user.id)
                # 配置新的权限
                for role_id in roles:
                    # if role == 0:
                    #     raise ApiError('ERROR_SET_MANAGER', error.ERROR_SET_MANAGER)
                    self.db_user_role_handle.make_new(user_id=user.id, role_id=role_id)

            # update
            self.db_handler.update(user, **update)
            db.session.commit()
        except:
            db.session.rollback()
            raise
