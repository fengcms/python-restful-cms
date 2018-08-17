#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 引用 /core/query.py 文件
from core import query
from core.tool import ok, fail, str2Hump

def ls (request, name):
    hmupName = str2Hump(name)
    res = query.ls(hmupName, request)
    if isinstance(res, dict):
        return ok(res)
    elif res == 404:
        return fail('数据库中没有' + name + '这个表', 404)
    elif res == 503:
        return fail('数据查询失败', 503)
    else:
        return fail('服务器内部错误', 500, 500)

def post (request, name):
    hmupName = str2Hump(name)
    res = query.post(hmupName, request)
    if isinstance(res, dict):
        return ok(res)
    elif res == 400:
        return fail('参数错误', 400)
    elif res == 404:
        return fail('数据库中没有' + name + '这个表', 404)
    elif res == 503:
        return fail('数据添加失败', 503)
    else:
        return fail('服务器内部错误', 500, 500)
