#!/usr/bin/env python3
# coding: utf8
# 20170220 anChaOs

import os, traceback, requests
from gevent import getcurrent


#dbg = print
def dbg(msg):
    print("<pid:{0},greenlet:{1}>dbg:{2}".format(os.getpid(), id(getcurrent()), msg))


def print_exception_info():
    # dbg(type(sys.exc_info()[1]))
    # dbg(sys.exc_info()[1])
    # dbg(sys.exc_info()[-1].tb_lineno)
    traceback.print_exc()


def send_sms_to_phone(phone, text):
    try:
        dbg("send_sms_to_phone")
        url = "http://112.74.76.186:8030/service/httpService/httpInterface.do"
        data = {"username":"JSM40444",
                "password":"uogngdg2",
                "veryCode":"9p3o03nvvaax",
                "method":"sendMsg",
                "mobile":phone,
                "content":"@1@={0}".format(text),
                "msgtype":"2",
                "tempid":"JSM40444-0014",
                "code":"utf-8"}

        r = requests.post(url, data=data)
        dbg(r.text)
        return r
    except:
        print_exception_info()
