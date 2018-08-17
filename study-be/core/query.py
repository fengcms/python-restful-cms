#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 从 db 文件夹中引用 model.py
from db import model

session = model.DBSession()

# 根据字符串判断数据库是否包含该表
def hasClass(className):
    try:
        getattr(model, className)
        return True
    except Exception as e:
        return False

# 将数据库查询数据变成字典型方法
def getDict(obj):
    res = {}
    for column in obj.__table__.columns:
        res[column.name] = getattr(obj, column.name)
    return res

# 查询列表方法
def ls(className, request):
    if not hasClass(className):
        return 404
    try:
        # 获得数据库类模型
        classModel = getattr(model, className)
        res = session.query(classModel).all()
        
        # 将结果整理成列表输出
        arr = []
        if res:
            for i in res:
                arr.append(getDict(i))
        return {'list': arr}
    except Exception as e:
        return 503
