#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
from sanic import Blueprint
from sanic.response import json
from config import PREFIX, ANONYMOUS_API as ANYAPI
from config import PRIVATE_KEY_PATH 
from config import UPLOAD_PATH, SUPPORT_TYPE

from core.tool import ok, fail, checkParam, getMd5, rsaDecrypt
from core.session import makeToken, checkToken, clearToken, updataToken
from core.app import listView, itemView
from core.handle import middleHandle
from core import rest


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

# 将菜单栏目以树形结构输出
@bp.route('tree_channel', methods=['GET'])
async def tree_channel(request):
    sourceData = rest.getList({'pagesize': -1, 'sort': '-sort,-id'}, 'channel')
    if sourceData == 1:
        return fail('服务器内部错误', 500, 500)
    if sourceData['total'] < 1:
        return fail('您当前还没有添加任何栏目')

    sourceList = sourceData['list']

    def makeTree(pid, arr):
        res = []
        for i in arr:
            if i['pid'] == pid:
                rep = makeTree(i['id'], arr)
                if len(rep) != 0:
                    i['children'] = rep
                res.append(i)
        return res
    res = makeTree(0, sourceList)

    return ok(res)

# 上传文件接口特殊处理
@bp.route('upload', methods=['POST'])
async def upload(request):
    # 字节码转16进制字符串
    def bytes2hex(bytes):
        hexstr = u""
        for i in range(10):
            t = u"%x" % bytes[i]
            if len(t) % 2:
                hexstr += u"0"
            hexstr += t
        return hexstr.lower()

    # 根据16进制字符串获取文件后缀
    def getSuffix(hexStr):
        print(hexStr)
        for i in SUPPORT_TYPE:
            if i in hexStr:
                return SUPPORT_TYPE[i]
        return 400

    # 判断参数是否正确
    if not request.files and not request.files.get('file'):
        return fail('参数错误', 400)
    image = request.files.get('file').body

    # 判断文件是否支持
    imageSuffix = getSuffix(bytes2hex(image))
    if imageSuffix == 400:
        return fail('不支持的文件类型', 400)

    # 组织图片存储路径
    md5Name = getMd5(image)

    saveDir = UPLOAD_PATH + md5Name[0:2] + '/'
    savePath = saveDir + md5Name[2:] + '.' + imageSuffix
    resPath = '/' + md5Name[0:2] + '/' + md5Name[2:] + '.' + imageSuffix

    # 如果文件夹不存在，就创建文件夹
    if not os.path.exists(saveDir):
        os.makedirs(saveDir)

    # 将文件写入到硬盘
    tempFile = open(savePath, 'wb')
    tempFile.write(image)
    tempFile.close()

    # 给客户端返回结果
    return ok({"path": resPath})
