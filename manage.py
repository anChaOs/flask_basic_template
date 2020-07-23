#!/usr/bin/env python3
#coding: utf8

import os, traceback

from flask_script import Manager, Shell
import sqlalchemy

from app import create_app, db
from app.database.model import User, Role, UserRole

from config import config

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db)
manager.add_command("shell", Shell(make_context=make_shell_context))


def init_database_and_tables():
    engine = sqlalchemy.create_engine('mysql+mysqlconnector://%s:%s@%s' % (
        config.MYSQL_USER, config.MYSQL_PASSWORD, config.MYSQL_IP))
    try:
        engine.execute("create database if not exists %s default character set utf8mb4 collate utf8mb4_unicode_ci" % config.DATABASE)
    except:
        traceback.print_exc()
    db.create_all()


def init_role():
    role = db.session.query(Role).filter(Role.name=='管理员').first()
    if role:
        return True
    role = Role(name='管理员')
    db.session.add(role)
    db.session.commit()


def init_admin_user():
    role = db.session.query(Role).first()
    if not role:
        print('no role init')
        raise Exception('no role init')

    user = User(name='admin')
    db.session.flush()
    user_role = UserRole(user_id=user.id, role_id=role.id)


@manager.command
def init():

    try:

        # 1. 创建数据库
        init_database_and_tables()

        # 2. 初始化用户角色
        init_role()

        # 3.创建管理员用户
        init_admin_user()

    except:

        traceback.print_exc()
        db.session.rollback()

if __name__ == '__main__':
    manager.run()