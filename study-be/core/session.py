#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import time
import random
import os
from core.tool import getMd5

TEMPPATH = 'temp/'

def makeToken (user, group, token=None):
    t = str(int(time.time()))
    if token == None:
        r = str(random.randint(10000, 99999))
        data = user + t + r
        token = getMd5(data)
    tokenPath = TEMPPATH + group + '_' + getMd5(user)
    os.system('echo ' + token + ',' + t + ' > ' + tokenPath)
    return user + '|' + group + '|' + token

def checkToken (tokenStr):
    # 检查传值是否为空
    if tokenStr == None:
        return 4
    tmp = tokenStr.split('|')
    
    # 检查传值是否符合我们的设计要求
    if len(tmp) != 3:
        return 4
    user = tmp[0]
    group = tmp[1]
    token = tmp[2]
    tokenPath = TEMPPATH + group + '_' + getMd5(user)
    
    # 检查服务器存储的对应 session 文件是否存在
    if not os.path.exists(tokenPath):
        return 4
    
    # 读取文件对比
    with open(tokenPath, 'r') as f:
        # 获取存储的各项值
        saveStrArr = str(f.read()).split(',')
        saveToken = saveStrArr[0]
        saveTime = int(saveStrArr[1])
        nowTime = int(time.time())
        
        # 看 token 值是否一致
        if token != saveToken:
            return 1
        # 看时间是否有效
        elif (nowTime - saveTime) > 3600:
            return 2
        # 正常
        else:
            return 0

def clearToken (tokenStr):
    tmp = tokenStr.split('|')
    if len(tmp) == 3:
        user = tmp[0]
        group = tmp[1]
        tokenPath = TEMPPATH + group + '_' + getMd5(user)
        os.system('rm ' + tokenPath)

def updataToken (tokenStr):
    tmp = tokenStr.split('|')
    if len(tmp) == 3:
        user = tmp[0]
        group = tmp[1]
        token = tmp[2]
        makeToken(user, group, token)

