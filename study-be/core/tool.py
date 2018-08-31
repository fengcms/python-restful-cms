#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sanic.response import json
from urllib.parse import unquote
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as CPK
import base64
import hashlib
import re

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

# 获取 md5 哈希值
def getMd5(source):
    if isinstance(source, str):
        source = source.encode('utf-8')
    m1 = hashlib.md5()
    m1.update(source)
    res = m1.hexdigest()
    return res

# 处理参数
def query2Dict(text):
    try:
        text = unquote(text)
        obj = dict([i.split('=') for i in text.split('&')]) 
        return obj
    except Exception as e:
        return {}

# 加密方法
def rsaEncrypt(keypath, string):
    with open(keypath, 'r') as f:
        pubkey = f.read()
        rsaKey = RSA.importKey(pubkey)
        cipher = CPK.new(rsaKey)
        res = base64.b64encode(cipher.encrypt(string.encode(encoding="utf-8")))
        return res.decode(encoding = 'utf-8')

# 解密方法
def rsaDecrypt(keypath, enCode):
    with open(keypath, 'r') as f:
        prikey = f.read()
        rsaKey = RSA.importKey(prikey)
        cipher = CPK.new(rsaKey)
        res = cipher.decrypt(base64.b64decode(enCode), "ERROR")
        return res.decode(encoding = 'utf-8')

# 下划线转驼峰
def str2Hump(text):
    arr = filter(None, text.lower().split('_'))
    res = ''
    for i in arr:
        res =  res + i[0].upper() + i[1:]
    return res

# 判断数字
def isInt(num):
    try:
        num = int(str(num))
        return isinstance(num, int)
    except:
        return False

def filterHtml(htmlStr):
    dr = re.compile(r'<[^>]+>', re.S)
    res = dr.sub('', htmlStr)
    return res

def dict2str(dictObj):
    res = ''
    sortKeys = sorted(dictObj.keys())
    for i in sortKeys:
        res += i + '=' + str(dictObj[i]) + '-'
    return res[0:-1]
