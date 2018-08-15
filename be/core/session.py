#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import hashlib
import time
import os
from core.tool import getMd5

TEMPPATH = 'temp/'

def makeSession (user, group, session=None):
    t = str(int(time.time()))
    if session == None:
        data = user + t
        session = getMd5(data)
    sessionPath = TEMPPATH + group + '_' + getMd5(user)
    os.system('echo ' + session + ',' + t + ' > ' + sessionPath)
    return user + '|' + group + '|' + session

def checkSession (session):
    if session == None:
        return 4
    tmp = session.split('|')
    user = tmp[0]
    group = tmp[1]
    session = tmp[2]
    sessionPath = TEMPPATH + group + '_' + getMd5(user)
    if os.path.exists(sessionPath):
        with open(sessionPath, 'r') as f:
            saveText = str(f.read()).split(',')
            saveSession = saveText[0]
            saveTime = int(saveText[1])
            nowTime = int(time.time())
            if session != saveSession:
                return 1
            elif (nowTime - saveTime) > 3600:
                return 2
            else:
                return 0

    else:
        return 4

def clearSession (session):
    tmp = session.split('|')
    user = tmp[0]
    group = tmp[1]
    sessionPath = TEMPPATH + group + '_' + getMd5(user)
    os.system('rm ' + sessionPath)

def updataSession (session):
    tmp = session.split('|')
    user = tmp[0]
    group = tmp[1]
    session = tmp[2]
    o = makeSession(user, group, session)
