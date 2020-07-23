#!/usr/bin/env python3
# coding: utf8
# 20170220 anChaOs


ERROR_OK = 0
ERROR_FAIL = 1
ERROR_PARAM = 2
ERROR_NO_TARGET = 3
ERROR_PERMISSION = 4

# auth
ERROR_NO_USER = 1001
ERROR_WRONG_PSWD = 1002
ERROR_NO_LOGIN = 1003
ERROR_USER_BANNED = 1004
ERROR_USER_EXIST = 1005

#database
ERROR_FAIL_CONNECT_DATABASE = 2001


error_info = {
  ERROR_OK: ('操作成功', 200),
  ERROR_FAIL: ('操作失败', 500),
  ERROR_PARAM: ('参数错误', 400),
  ERROR_NO_TARGET: ('目标不存在', 422),

  ERROR_NO_USER: ('用户不存在', 422),
  ERROR_WRONG_PSWD: ('密码错误', 422),
  ERROR_NO_LOGIN: ('未登录', 401),
  ERROR_USER_BANNED: ('用户暂不可用', 422),
  ERROR_USER_EXIST: ('用户已存在', 422),

  ERROR_FAIL_CONNECT_DATABASE : ('服务器开小差了，请稍后重试', 500),

}

def get_error_info(error_no):
    if error_no in error_info:
        return error_info[error_no]
    else:
        return ("操作失败", 500)

def get_error_status_code(error_no):
    if error_no in error_status_code:
        return error_status_code[error_no]
    else:
        return ""

class ApiError(Exception):
    def __init__(self, msg, error_no=1):
        self.msg = msg
        self.error_no = error_no
        
    def __str__(self):
        return repr(self.msg)