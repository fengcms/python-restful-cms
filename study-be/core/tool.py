#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sanic.response import json
from urllib.parse import unquote
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as CPK
import hashlib

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
