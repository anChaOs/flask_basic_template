#!/usr/bin/env python3
# coding: utf8
# 20170220 anChaOs

import json

from datetime import datetime, timedelta
# from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import LONGTEXT

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db, lm
from config import config

from app.tool import dbg                    # for print
from app.tool import print_exception_info   # for traceback

def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


db.Model.to_dict = to_dict


class User(db.Model, UserMixin):
    """
        @ 用户表

    """
    __tablename__ = 'user'

    id                  = db.Column(db.Integer, primary_key=True)
    name                = db.Column(db.String(32), nullable=False, server_default='')
    avatar              = db.Column(db.String(128), nullable=False, server_default='')
    banned              = db.Column(db.Integer, nullable=False, server_default='0')

    ctime   = db.Column(db.DateTime, nullable=False, server_default=func.now())
    utime   = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    status  = db.Column(db.Integer, nullable=False, server_default='0')

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % self.name

    def to_dict(self):
        resp_dict = {
            "id": self.id,
            "name": self.name,
            "avatar": self.avatar,
            "status": self.status,
            "banned": self.banned
        }
        return resp_dict

@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class UserWechat(db.Model):
    """
        @ 用户微信信息表
    """
    __tablename__ = 'user_wechat'

    id          = db.Column(db.Integer, primary_key=True)
    user_id     = db.Column(db.ForeignKey(u'user.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)
    openid      = db.Column(db.String(256), index=True, nullable=False, server_default="")
    unionid     = db.Column(db.String(256), index=True, nullable=False, server_default="")
    nickname    = db.Column(db.String(128), nullable=True, server_default="")
    sex         = db.Column(db.String(1), nullable=False, server_default="0")
    province    = db.Column(db.String(64), nullable=False, server_default="")
    city        = db.Column(db.String(64), nullable=False, server_default="")
    country     = db.Column(db.String(64), nullable=False, server_default="")
    headimgurl  = db.Column(db.String(512), nullable=False, server_default="")
    privilege   = db.Column(db.String(512), nullable=False)
    ctime       = db.Column(db.DateTime, nullable=False)
    utime       = db.Column(db.DateTime, nullable=False)

    status      = db.Column(db.Integer, nullable=False, server_default="0")


class UserAuth(db.Model):
    """
        @ 用户授权信息表

            identity_source     授权来源    : 0本站 1第三方
            identity_type       登录类型    : phone/email/username/weixin/ali/weibo  ...
            identifier          登陆标示    : 手机号/邮箱/用户名/微信openid/阿里openid  ...
            credential          密码凭证    : 密码 or token

    """
    __tablename__ = 'user_auth'

    id              = db.Column(db.Integer, primary_key=True)
    user_id         = db.Column(db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    identity_source = db.Column(db.Integer, nullable=False, server_default='0')
    identity_type   = db.Column(db.String(16), nullable=False)
    identifier      = db.Column(db.String(128), nullable=False)
    credential      = db.Column(db.String(256), nullable=False)

    login_time      = db.Column(db.DateTime, nullable=False, server_default=func.now())

    ctime   = db.Column(db.DateTime, nullable=False, server_default=func.now())
    utime   = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    status  = db.Column(db.Integer, nullable=False, server_default='0')

    def __init__(self, user_id, identity_source, identity_type, identifier, credential):
        self.user_id = user_id
        self.identity_source = identity_source
        self.identity_type = identity_type
        self.identifier = identifier
        if identity_source == 0:
            self.credential = generate_password_hash(credential)
        else:
            self.credential = credential

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        if self.identity_source == 0:
            self.credential = generate_password_hash(password)
        else:
            raise AttributeError('no password attribute')

    def verify_password(self, password):
        if self.identity_source == 0:
            return check_password_hash(self.credential, password)
        else:
            raise AttributeError('no password attribute')

    def __repr__(self):
        return '<UserAuth user_id:%r identity_type: %r>' % (self.user_id, self.identity_type)


class Role(db.Model):
    """
        角色表
            name    角色名称
            desc    角色描述
    """
    __tablename__ = 'role'

    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(16), nullable=False, server_default='')
    desc        = db.Column(db.String(128), nullable=False, server_default='')

    ctime       = db.Column(db.DateTime, nullable=False, server_default=func.now())
    utime       = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    status      = db.Column(db.Integer, nullable=False, server_default='0')


class UserRole(db.Model):
    """
        用户角色表
    """
    __tablename__ = 'user_role'

    id          = db.Column(db.Integer, primary_key=True)
    user_id     = db.Column(db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    role_id     = db.Column(db.Integer, nullable=False, server_default='0')

    ctime       = db.Column(db.DateTime, nullable=False, server_default=func.now())
    utime       = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    status      = db.Column(db.Integer, nullable=False, server_default='0')

    def __repr__(self):
        return '<UserRole %r>' % self.id


class LoginToken(db.Model):
    """
        @ 登陆token表
    """
    __tablename__ = 'login_token'

    id          = db.Column(db.Integer, primary_key=True)
    token       = db.Column(db.String(128), nullable=False, server_default='', unique=True)

    ctime       = db.Column(db.DateTime, nullable=False, server_default=func.now())
    utime       = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    status      = db.Column(db.Integer, nullable=False, server_default='0')

    def __repr__(self):
        return '<LoginToken :%r>' % self.id

