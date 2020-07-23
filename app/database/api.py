#!/usr/bin/env python3
# coding: utf8
# 20170220 anChaOs

import json, time, traceback
from functools import wraps
import sqlalchemy
from sqlalchemy import or_

from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from app import db
from .model import *

from app.tool import dbg                    # for print
from app.tool import print_exception_info   # for traceback

# error
import app.error as error
ApiError = error.ApiError


"""
    @ 最新变动
    1. 所有的db.session将统一在view中commit

"""


class DatabaseError(Exception):
    def __init__(self, msg="", error_no=0):
        self.msg = msg
        self.error_no = error_no
        
    def __str__(self):
        return repr(self.msg)


def catch_except(func):
    @wraps(func)
    def wrapper(*args, **kws):
        try:
            return func(*args, **kws)
        except ApiError as e:
            raise e
        except sqlalchemy.exc.DatabaseError as e:
            db.session.rollback()
            print_exception_info()
            if 'page' in kws and 'psize' in kws:
                return 0, None
            return None
        except:
            print_exception_info()
            if 'page' in kws and 'psize' in kws:
                return 0, None
            return None
    return wrapper


def need_model(func):
    @wraps(func)
    def wrapper(self, *args, **kws):
        if not self.Model:
            dbg('not init model yet')
            raise DatabaseError('not init model yet')
        return func(self, *args, **kws)
    return wrapper


class DbapiModel():

    def __init__(self):
        self.Model = None

    @need_model
    def _make_new_common(self, **kwargs):
        obj = self.Model(**kwargs)
        db.session.add(obj)
        return obj

    @need_model
    def _update_common(self, obj, **kwargs):
        # dbg((Model, obj, kwargs))
        query = db.session.query(self.Model).filter(self.Model.id==obj.id)
        count = query.update(kwargs)
        # dbg(count)
        return obj

    @need_model
    def _model_filter(self, query, **kwargs):
        for attr in self.Model.__table__.columns:
            if attr.name in kwargs:
                query = query.filter(getattr(self.Model, attr.name)==kwargs[attr.name])
        return query

    @need_model
    def _model_one_query(self, query, **kwargs):
        if 'id' in kwargs:
            return query.first()
        return 'not one query'

    @need_model
    def _query_by_page_common(self, query, **kwargs):
        if 'page' in kwargs and 'psize' in kwargs:
            page = int(kwargs['page'])
            psize = int(kwargs['psize'])
            return query.with_entities(func.count(self.Model.id)).scalar(), \
                query.slice(psize*(page-1), psize*page).all()
        else:
            return query.all()

    @need_model
    def _get_common(self, query, **kwargs):
        # 筛选
        query = self._model_filter(query, **kwargs)

        # 排序
        if 'sorter' in kwargs:
            # 包含排序字段和排序方式
            # ?sorter=-ctime,sort
            sorter = kwargs['sorter']
            try:
                attrs = sorter.split(',') or []
                for attr in attrs:
                    if attr[0] == '-':
                        query = query.order_by(getattr(self.Model, attr[1:]).desc())
                    else:
                        query = query.order_by(getattr(self.Model, attr))
            except:
                dbg(sorter)
                print_exception_info()

        # 单条数据查询
        obj = self._model_one_query(query, **kwargs)
        if obj != 'not one query':
            return obj
        # 是否分页
        return self._query_by_page_common(query, **kwargs)

    def make_new(self, **kwargs):
        return self._make_new_common(**kwargs)

    def update(self, obj, **kwargs):
        return self._update_common(obj, **kwargs)

    @need_model
    def get(self, **kwargs):
        query = db.session.query(self.Model)
        if getattr(self.Model, 'deleted', None) is not None:
            query = query.filter(self.Model.deleted==0)

        return self._get_common(query, **kwargs)


class DbapiUser(DbapiModel):

    def __init__(self):
        self.Model = User

    @need_model
    def _model_filter(self, query, **kwargs):
        query = super(DbapiUser, self)._model_filter(query, **kwargs)
        return query

    def _model_one_query(self, query, **kwargs):
        obj = super(DbapiUser, self)._model_one_query(query, **kwargs)
        if obj and obj != 'not one query':
            return obj

        if 'name' in kwargs:
            return query.first()
        if 'phone' in kwargs:
            return query.first()
        if 'openluat_user_id' in kwargs:
            return query.first()

        return 'not one query'


class DbapiUserWechat(DbapiModel):

    def __init__(self):
        self.Model = UserWechat


class DbapiUserAuth(DbapiModel):

    def __init__(self):
        self.Model = UserAuth

    def _model_one_query(self, query, **kwargs):
        obj = super(DbapiUserAuth, self)._model_one_query(query, **kwargs)
        if obj and obj != 'not one query':
            return obj

        if 'id' in kwargs:
            return query.first()
        if 'identity_type' in kwargs and 'identifier' in kwargs:
            return query.first()
        if 'identity_type' in kwargs and 'user_id' in kwargs:
            return query.first()

        return 'not one query'


class DbapiUserRole(DbapiModel):

    def __init__(self):
        self.Model = UserRole

    def delete_user_roles(self, user_id):
        user_roles = self.get(user_id=user_id) or []
        for user_role in user_roles:
            db.session.delete(user_role)


class DbapiLoginToken(DbapiModel):

    def __init__(self):
        self.Model = LoginToken


class Dbapi():

    def __init__(self):
        all_vars = globals()
        for k, v in all_vars.items():
            if not isinstance(v, type):
                continue
            if issubclass(v, DbapiModel):
                setattr(self, k[5:], v())
                # print(k, v, type(v))
        print('over...')

dbapi = Dbapi()