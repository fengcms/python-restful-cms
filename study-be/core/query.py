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

# 查询单条数据方法
def get(className, oid):
    if not hasClass(className):
        return 404
    try:
        classModel = getattr(model, className)
        res = session.query(classModel)
        if oid == 'first':
            res = res.first()
            if res == None:
                return 4043
            else:
                return getDict(res)
        else:
            res = res.filter_by(id=oid)
            try:
                res = res.one()
                return getDict(res)
            except Exception as e:
                return 4042

    except Exception as e:
        return 503

# 修改数据方法
'''
1. 支持未知ID单条数据修改
    URL:    /xxx/first
    DATA:   {...}
    此方法会找数据库第一条数据，进行对应修改，用于特殊用途
2. 支持单ID数据修改
    URL: /xxx/:id
    DATA:   {...}
    正常使用，数据为需要修改的数据字典
3. 支持多ID单数据修改
    URL: /xxx/1,2,3,4,5,6
    DATA:   {...}
    支持将多条数据的内容进行统一处理，例如批量加入回收站或者批量转移归属栏目等
4. 支持多ID多数据修改
    URL: /xxx/batch
    DATA:   {'data': [{...}, {...}, {...}, {...}]}
    将需要多条修改的数据构成数组，用 'data' 字段传进来。
    每个数据里面必须包含 'id' 字段，否则参数错误
'''
def put(className, oid, data):
    if not hasClass(className):
        return 404

    # 构建成功和失败 id 数据
    succIds = []
    failIds = []

    # 修改数据方法
    def putData(res, id, dat = data):
        if res:
            oldData = getDict(res)
            # ID 不可修改，所以移除 ID 数据
            if 'id' in dat:
                dat.pop('id')

            for i in dat:
                setattr(res, i, dat[i])

            session.add(res)
            session.commit()
            succIds.append(oldData['id'])
        else:
            failIds.append(id)

    try:
        classModel = getattr(model, className)
        res = session.query(classModel)

        fields = getFieldList(classModel)

        # 处理不知道ID的单条数据修改
        if oid == 'first':
        
            # 检查提交数据是否合法
            if not checkField(data, fields):
                return 400

            putData(res.first(), -1)
        # 处理多条数据批量修改
        elif oid == 'batch':
            
            # 如果没有获取到批量修改的数据则返回参数错误
            if not data.get('data'):
                return 400
                
            dat = data['data']
            
            # 循环批量修改数据，检查数据是否合法
            for i in dat:
                if not checkField(i, fields):
                    return 400
                if not 'id' in i:
                    return 400

            # 循环数据，逐一修改
            for i in dat:
                putData(res.get(i['id']), i['id'], i)

        # 处理正常单条数据单ID或多ID批量修改
        else:
            # 检查提交数据是否合法
            if not checkField(data, fields):
                return 400
            
            # 拆解 id 组成数据（一个和多个是一样的）
            idArr = oid.split(',')
            for id in idArr:
                putData(res.get(id), int(id))
        # 如果修改成功的 ID 数为 0 ，则说明参数错误
        # 否则返回成功的 ID 和失败的 ID
        if len(succIds) == 0:
            return 400
        else:
            return {'success': succIds, 'fail': failIds}

    except Exception as e:
        return 503
