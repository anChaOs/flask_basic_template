#!/usr/bin/env python3
# 20170119 anChaOs

import os

MONGODB_ADDRESS  = "mongodb://localhost:27017"
DEFAULT_PASSWORD = '888888'
PROJECT_NAME = ''

if os.environ.get("production"):
# if 1:
    print('"[Environ] 正式环境 ..."')

    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'password'
    MYSQL_IP = '127.0.0.1'
    DATABASE = PROJECT_NAME

    API_SITE_PREFIX     = '/site'
    API_BACKEND_PREFIX  = '/backend'


else:
    print('"[Environ] 测试环境 ..."')

    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'password'
    MYSQL_IP = '127.0.0.1'
    DATABASE = PROJECT_NAME

    API_SITE_PREFIX     = '/site'
    API_BACKEND_PREFIX  = '/backend'


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'NeverToldYou1234567890'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'mongodb'
    SESSION_KEY_PREFIX = '%s_' % PROJECT_NAME # 不同项目用不同前缀
    SESSION_USE_SIGNER = True
    SESSION_MONGODB_DB = 'common_data'
    SESSION_MONGODB_COLLECT = '%s_session' % PROJECT_NAME

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'mysql+mysqlconnector://%s:%s@%s/%s' % (MYSQL_USER, MYSQL_PASSWORD, MYSQL_IP, DATABASE)
    SQLALCHEMY_POOL_RECYCLE = 60

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass


config_list = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
