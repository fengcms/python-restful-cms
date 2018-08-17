#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sanic import Blueprint
from sanic.response import json
from config import PREFIX, ANONYMOUS_API as ANYAPI
from config import PRIVATE_KEY_PATH 

from core.tool import ok, fail, checkParam
from core.tool import rsaDecrypt
from core.session import makeToken, checkToken, clearToken, updataToken
from core.app import listView, itemView
from core.handle import middleHandle


FIX = PREFIX['be']
# 创建 蓝图
bp = Blueprint('be', url_prefix=FIX)

# 加载默认 rest 接口生成路由
bp.add_route(listView.as_view(), '<name>')
bp.add_route(itemView.as_view(), '<name>/<oid>')

@bp.middleware('request')
async def check(request):
    rep = middleHandle(request, FIX, ANYAPI)
    if rep:
        return rep

# 登录接口
@bp.route('login', methods=['POST'])
async def login(request):
    dat = request.json
    manageData = {'username': 'admin', 'password': '123456'}

    res = fail('参数错误', 400)

    # 检查入参是否正确
    if not checkParam(['account', 'password'], dat):
        del res.cookies['session']
        return res

    # 从传参中解密密码
    password = rsaDecrypt(PRIVATE_KEY_PATH, dat['password'])

    # 检查用户名密码是否正确
    if dat['account'] != manageData['username'] \
            or password != manageData['password']:
        res = fail('用户名或密码错误', 400)
        del res.cookies['session']
        return res

    # 正常处理
    token = makeToken(dat['account'], 'manage')
    res = ok(token)
    res.cookies['session'] = token
    res.cookies['session']['httponly'] = True

    return res

# 登出处理
@bp.get("logout")
async def logout(request):
    token = request.cookies.get('session')
    res = fail('退出失败', 401, 401)
    cs = checkToken(token)
    if cs == 0:
        clearToken(token)
        res = ok('退出成功')
    del res.cookies['session']
    return res
