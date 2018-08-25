#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 引用 /core/query.py 文件
import json
from core import query
from core.tool import ok, fail, str2Hump
from config import REDIS_CONFIG, REDIS_SPEED_TIME
import redis

try:
    r = redis.Redis(**REDIS_CONFIG)
    r.dbsize()
except:
    r = None

def getList (request, name):
    data = json.loads(ls(request, name).body)
    if data['status'] == 0:
        return data['data']
    return 1

def getItem (name, oid):
    data = json.loads(get({}, name, oid).body)
    if data['status'] == 0:
        return data['data']
    return 1

def ls (request, name, key, speed):
    hmupName = str2Hump(name)

    if r != None and r.get(key) and speed:
        res = json.loads(r.get(key))
        print('get by redis')
    else:
        res = query.ls(hmupName, request)
        print('get by db')
        if speed and r != None:
            r.set(key, json.dumps(res), ex=REDIS_SPEED_TIME)

    if isinstance(res, dict):
        return ok(res)
    elif res == 400:
        return fail('参数错误', 400)
    elif res == 404:
        return fail('数据库中没有' + name + '这个表', 404, 404)
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
        return fail('数据库中没有' + name + '这个表', 404, 404)
    elif res == 503:
        return fail('数据添加失败', 503)
    else:
        return fail('服务器内部错误', 500, 500)

def get (request, name, oid, key, speed):
    hmupName = str2Hump(name)

    if r != None and r.get(key) and speed:
        res = json.loads(r.get(key))
        print('get by redis')
    else:
        res = query.get(hmupName, oid)
        print('get by db')
        if speed and r != None:
            r.set(key, json.dumps(res), ex=REDIS_SPEED_TIME)

    if isinstance(res, dict):
        return ok(res)
    elif res == 404:
        return fail('数据库中没有' + name + '这个表', 404, 404)
    elif res == 4042:
        return fail('没有这条数据', 404, 404)
    elif res == 4043:
        return fail(name + '数据库中没有数据', 404, 404)
    elif res == 503:
        return fail('数据查询失败', 503)
    else:
        return fail('服务器内部错误', 500, 500)

def put (request, name, oid):
    hmupName = str2Hump(name)
    res = query.put(hmupName, oid, request)
    if isinstance(res, dict):
        return ok(res)
    elif res == 400:
        return fail('参数错误', 400)
    elif res == 404:
        return fail('数据库中没有' + name + '这个表', 404, 404)
    elif res == 503:
        return fail('数据更新失败', 503)
    else:
        return fail('服务器内部错误', 500, 500)

def delete (request, name, oid):
    hmupName = str2Hump(name)
    res = query.delete(hmupName, oid)
    if isinstance(res, dict):
        return ok(res)
    elif res == 400:
        return fail('您要删除的数据不存在', 400)
    elif res == 404:
        return fail('数据库中没有' + name + '这个表', 404, 404)
    elif res == 503:
        return fail('数据删除失败', 503)
    else:
        return fail('服务器内部错误', 500, 500)
