#!/usr/bin/env python3
# coding: utf8
# 20170220 anChaOs


import json
import time
import requests
import string
import random
import traceback

from datetime import datetime

from app.tool import dbg                    # for print
from app.tool import print_exception_info   # for traceback

# error
import app.error as error
ApiError = error.ApiError

# db
from app import db

# config
import config as config

# database functions
import app.database.api as dbapi


def to_dict(self):
  return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


def get_trode_no():
    max_id = dbapi.get_max_pay_id()
    str_max_id = '%04d' % max_id
    if len(str_max_id) > 4:
        str_max_id = str_max_id[-4:]
    return 'G' + datetime.now().strftime("%Y%m%d%H%M%S") + str_max_id