#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sanic.response import json

# 成功返回
def ok(data):
    return json({"data": data, "status": 0})

# 失败返回
def fail(data, statusCode=1, httpCode=200):
    return json({"data": data, "status": statusCode}, status=httpCode)

# 检查参数
def checkParam(params, req):
    if not isinstance(params, list):
        return False
    if not isinstance(req, dict):
        return False

    for i in params:
        if not i in req:
            return False

    return True
