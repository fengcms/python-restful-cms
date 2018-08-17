#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sanic import Blueprint
from sanic.response import json
from config import PREFIX

from core.tool import ok, fail, checkParam
from core.session import makeToken, checkToken, clearToken, updataToken

FIX = PREFIX['be']
# 创建 蓝图
bp = Blueprint('be', url_prefix=FIX)

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

    # 检查用户名密码是否正确
    if dat['account'] != manageData['username'] \
            or dat['password'] != manageData['password']:
        res = fail('用户名或密码错误', 400)
        del res.cookies['session']
        return res

    # 正常处理
    session = makeToken(dat['account'], 'manage')
    res = ok(session)
    res.cookies['session'] = session
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
