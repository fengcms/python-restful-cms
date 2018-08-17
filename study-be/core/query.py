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

# 传入模型，获得该模型字段列表, 用于 ls 方法
def getFieldList(Obj):
    res = []
    for i in dir(Obj):
        if i[0] != '_':
            res.append(i)
    return res

# 传入模型，获得该模型字段字典并赋空值，排除id和time，用于post方法
def getFieldDict(Obj):
    res = {}
    for i in dir(Obj):
        if i[0] != '_' and i != 'id' and i != 'time':
            res[i] = ''
    return res

# 检查提交数据字段是否在表中包含方法
def checkField(dat, fields):
    for i in dat:
        if not i in fields:
            return False
    return True

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

# 添加新数据方法
def post(className, request):
    if not hasClass(className):
        return 404
    try:
        classModel = getattr(model, className)

        # 检查数据是否符合模型字段要求
        fields = getFieldList(classModel)
        for Data in request['data']:
            if not checkField(Data, fields):
                return 400
        
        # 添加数据
        resIds = []
        modelDict = getFieldDict(classModel)
        for Data in request['data']:
            for i in Data:
                # POST 时传的 id 和 time 字段会被忽略
                if i != 'id' and i != 'time':
                    modelDict[i] = Data[i]
            newData = classModel(**modelDict)
            session.add(newData)
            session.flush()
            session.commit()
            resIds.append(newData.id)
        # 将自增ID返回
        return {'id': resIds}
    except Exception as e:
        return 503
