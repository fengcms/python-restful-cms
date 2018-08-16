#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sanic import Blueprint
from sanic.response import json
from config import PREFIX

from core.tool import ok, fail, checkParam

FIX = PREFIX['be']
# 创建 蓝图
bp = Blueprint('be', url_prefix=FIX)

# 登录接口
@bp.route('login', methods=['POST'])
async def login(request):
    dat = request.json
    manageData = {'username': 'admin', 'password': '123456'}

    # 检查入参是否正确
    if not checkParam(['account', 'password'], dat):
        return fail('参数错误', 400)

    if dat['account'] != manageData['username'] \
            or dat['password'] != manageData['password']:
        return fail('用户名或密码错误', 400)
    return ok('登录成功')

