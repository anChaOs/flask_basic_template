#!/usr/bin/env python3
# coding: utf8
# 20170522 anChaOs

import requests
import json
import hashlib  # for md5
import traceback
import time
import string, random, sys

from datetime import datetime, timedelta


class SimuRequest(object):

    def __init__(self):
        self.http_session = requests.Session()

        self.DEBUG = 2  # 0正式 1测试 2开发
        if self.DEBUG == 2:
            self.BASE_URL = 'http://localhost:5000'
        elif self.DEBUG == 1:
            self.BASE_URL = 'http://test.community.openluat.com/api'
        elif self.DEBUG == 0:
            self.BASE_URL = 'http://community.openluat.com/api'

    def _deal_with_response(self, r):
        if r.status_code == requests.codes.ok:
            try:
                # print(r.json())
                print(json.dumps(r.json(), indent=4, ensure_ascii=False))
                return r.json()
            except:
                print(r.text)
        else:
            print('status_code: ', r.status_code)
            try:
                # print(r.json())
                print(json.dumps(r.json(), indent=4, ensure_ascii=False))
                return r.json()
            except:
                print(r.text)

    def _http_request(self, method, path, **kwargs):
        url = self.BASE_URL + path
        if method == 'get':
            r = self.http_session.get(url, **kwargs)
        elif method == 'post':
            r = self.http_session.post(url, **kwargs)
        elif method == 'put':
            r = self.http_session.put(url, **kwargs)
        else:
            print('wrong method')
            return
        return self._deal_with_response(r)

    def get(self, path, **kwargs):
        return self._http_request('get', path, **kwargs)

    def post(self, path, **kwargs):
        return self._http_request('post', path, **kwargs)

    def put(self, path, **kwargs):
        return self._http_request('put', path, **kwargs)

    def test(self):
        path = '/test/test'
        payload = {
            'test': 'test'
        }
        self.post(path, json=payload)

    def unlogin(self):
        path = '/auth/unlogin'
        self.get(path)

    def login(self):
        path = '/auth/login'
        payload = {
            'username': '15313112713',
            'password': '123456'
        }
        self.post(path, json=payload)

    def cur(self):
        path = '/auth/cur'
        self.get(path)

    def logout(self):
        path = '/auth/logout'
        self.post(path)

    def captcha(self):
        path = '/auth/captcha'
        payload = {
            'phone': '18001722713'
        }
        self.post(path, json=payload)

    def reset_password(self):
        path = '/auth/reset_password'
        payload = {
            'phone': '18001722713',
            'code': '898651',
            'password': '888888'
        }
        self.post(path, json=payload)


def main():
    simu = SimuRequest()
    # simu.test()
    # simu.unlogin()
    # simu.login()
    # simu.cur()
    # simu.logout()
    # simu.cur()
    # simu.captcha()
    simu.reset_password()


if __name__ == '__main__':
    main()