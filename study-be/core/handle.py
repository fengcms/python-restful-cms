#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from core.session import makeToken, checkToken, clearToken, updataToken
from core.tool import fail

def middleHandle(request, prefix, anyList=[]):
    rUrl = request.url
    # 检查请求路径中是否包含前缀
    if not prefix in rUrl:
        return fail('请求路径不合法', 404, 404)
    
    '''
    将请求路径去掉接口前缀之前的内容
    再去掉路径 ? 号后面追加的参数
    再用 / 斜线拆分成列表
    例如 http://0.0.0.0:8000/api/v1/be/love/102
    这样的地址，会得到 ['love', '102'] 这样的列表
    '''
    urlArr = list(filter(None, rUrl.split(prefix)[1].split('?')[0].split('/')))
    method = request.method
    apiName = urlArr[0].lower()
    
    # 检查是否符合我们的设计要求，我们只允许 /xxx 或 /xxx/:id 这样的两种结构
    if len(urlArr) == 0 or len(urlArr) > 2:
        return fail('请求路径不合法', 404, 404)
    
    # 全局请求方法检查
    if len(urlArr) == 1 and not method in ['GET', 'POST']:
        return fail('不被允许的请求方法', 405, 405)
    if len(urlArr) == 2 and not method in ['GET', 'PUT', 'DELETE']:
        return fail('不被允许的请求方法', 405, 405)
    
    # 检查是否登录
    checkLogin = True
    
    for i in anyList:
        if apiName == i.lower():
            checkLogin = False
    
    if checkLogin:
        token = request.cookies.get('session')
        cs = checkToken(token)
        if cs == 1:
            return fail('没有权限', 401, 401)
        elif cs == 2:
            return fail('登录超时', 401, 401)
        elif cs == 4:
            return fail('请重新登录', 401, 401)
        elif cs == 0:
            updataToken(token)
