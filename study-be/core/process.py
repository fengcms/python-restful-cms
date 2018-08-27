#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from core.tool import ok, dict2str
from core import rest
import json
# 引入配置文件中的前缀参数
from config import PREFIX, REDIS_SPEED_API_PREFIX_LIST

# 加载前后处理模块
async def doProcess(app, name, request, query, method, oid=None):
    # 是否需要缓存加速，默认否
    speed = False
    # 通过配置前缀字典，获得不同前缀字符串，并替换斜杠为下划线
    for i in PREFIX:
        if i in request.url:
            FIX = PREFIX[i]
            p = '_'.join(list(filter(None, FIX.split('/'))))
            # 查看接口是否在加速列表
            if FIX in REDIS_SPEED_API_PREFIX_LIST:
                speed = True
    
    # 组装前后处理的不同名称
    bm = p + 'before' + name
    am = p + 'after' + name

    # 进行对应前处理，非字典结果，直接抛出
    if dir(app.process.get(bm)).count(method) == 1:
        if oid == None:
            data = await getattr(app.process.get(bm), method)(query)
        else:
            data = await getattr(app.process.get(bm), method)(query, oid)

        if data:
            return data

    # 得到查询结果
    if oid == None:
        if method == 'ls':
            redisKeyName = p + name + dict2str(query)
            response = getattr(rest, method)(query, name, redisKeyName, speed)
        else:
            response = getattr(rest, method)(query, name)
    else:
        if method == 'get':
            redisKeyName = p + name + oid + dict2str(query)
            response = getattr(rest, method)(query, name, oid, redisKeyName, speed)
        else:
            response = getattr(rest, method)(query, name, oid)

    resBody = json.loads(response.body)
    resStatus = response.status
    # 根据返回结果判断是否需要后处理(错误状态就不处理了)
    if resStatus == 200 and resBody['status'] == 0 \
            and dir(app.process.get(am)).count(method) == 1:
        data = await getattr(app.process.get(am), method)(resBody['data'])
        return ok(data)
    else:
        return response
