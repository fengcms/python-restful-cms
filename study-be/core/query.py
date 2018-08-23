#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 从 db 文件夹中引用 model.py
from db import model
# 在配置中，获取默认分页条数参数
from config import PAGESIZE
# 从工具中引入判断是否是数字方法
from core.tool import isInt

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
        # 从请求参数中获取非标准参数
        args = {}
        for i in request:
            i = i.lower()
            if not i in ['page', 'pagesize', 'sort', 'time']:
                args[i] = request[i]

        # 获得模型，以及支持的字段数组列表
        classModel = getattr(model, className)
        modelList = getFieldList(classModel)

        # 开始查询数据
        res = session.query(classModel)
        
        # 处理时间参数
        if 'time' in request:
            
            # 将时间参数用短横线拆成数组
            tArr = request['time'].split('-')
            
            # 如果数组长度大于2，就说明传了错误的参数
            if len(tArr) > 2:
                return 400
            
            # 循环数组，看值是否是数字，否则参数错误
            for i in tArr:
                if not isInt(i):
                    return 400
            
            # 如果只有一个数字，则需要根据这个数值计算当天的0点和24点的时间戳
            if len(tArr) == 1:
                t = int(tArr[0])
                
                # 这个算法完全是用算术来计算的，以中国时区偏差做了调整
                # 更多内容请搜索时间戳的相关资料
                st = t - (t + 28800)%86400
                et = st + 86400
            else:
                st = int(tArr[0])
                et = int(tArr[1])
                
            field = getattr(classModel, 'time')
            res = res.filter(field < et).filter(field >= st)

        # 处理各种非标准参数查询
        for i in args:
        
            # 支持一个条件带多个参数，用英文逗号分割
            argVal = args[i].split(',')
            
            # 参数分为两部分，字段名和方法用短横线分割
            # 所以，这里把参数用短横线分割成数组
            arg = i.split('-')
            
            # 如果参数名中有多个短横线，则表示参数错误
            if len(arg) > 2:
                return 400
            
            # 从参数中取出字段名 
            argField = arg[0]
            
            # 取出特殊查询条件。如果没有短横线后面的内容，则为 None
            argMethod = None if len(arg) == 1 else arg[1]
            
            # 字段模型，用 getattr 函数获取
            field = getattr(classModel, argField)
            
            # 检查字段是否是模型支持的
            if not argField in modelList:
                return 400
            
            # 处理特殊查询条件
            if argMethod:
                # 模糊查询
                if argMethod == 'like':
                    for val in argVal:
                        res = res.filter(field.like('%' + val + '%'))
                # 不等于查询
                elif argMethod == 'neq':
                    for val in argVal:
                        res = res.filter(field != val)
                # 大于查询
                elif argMethod == 'gt' and len(argVal) == 1:
                    res = res.filter(field > argVal[0])
                # 大于等于查询
                elif argMethod == 'gteq' and len(argVal) == 1:
                    res = res.filter(field >= argVal[0])
                # 小于查询
                elif argMethod == 'lt' and len(argVal) == 1:
                    res = res.filter(field < argVal[0])
                # 小于等于查询
                elif argMethod == 'lteq' and len(argVal) == 1:
                    res = res.filter(field <= argVal[0])
                # in List 查询
                elif argMethod == 'in':
                    res = res.filter(field.in_(argVal))
                # not in List 查询
                elif argMethod == 'nin':
                    res = res.filter(~field.in_(argVal))
                # 其他不支持关键词返回参数错误
                else:
                    return 400
            # 处理普通相等查询条件
            else:
                for val in argVal:
                    res = res.filter(field == val)

        # 获取排序参数
        sort = 'id' if not 'sort' in request else request['sort']

        # 支持多重条件排序，用英文逗号分隔
        sortArr = sort.split(',')
        for i in sortArr:
            # 根据排序参数第一个字符是否是中划线确定是正序还是倒序，为假倒序
            sortType = i[0] == '-'
            sortField = i[1:] if sortType else i

            field = getattr(classModel, sortField)

            if not sortField in modelList:
                return 400
                
            if sortType:
                res = res.order_by(field)
            else:
                res = res.order_by(field.desc())

        # 统计总条数
        total = res.count()

        # 获取分页序号参数
        page = 0 if not 'page' in request else request['page']
        if not isInt(page):
            return 400
        else:
            page = int(page)

        # 获取分页每页数量参数
        pagesize = PAGESIZE if not 'pagesize' in request else request['pagesize']
        if not isInt(pagesize):
            return 400
        else:
            pagesize = int(pagesize)

        # 处理分页和分页需要查询 如果 pagesize 为 -1 则全部输出
        if pagesize == -1:
            res = res.all()
        else:
            res = res.limit(pagesize).offset(page * pagesize)

        # 将结果整理成列表输出
        arr = []
        if res:
            for i in res:
                arr.append(getDict(i))
        return {'list': arr, 'total': total}

    except Exception as e:
        print(e)
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
        for Data in request['data']:
            # POST 时传的 id 和 time 字段会被忽略
            if 'id' in Data:
                Data.pop('id')
            if 'time' in Data:
                Data.pop('time')
                
            newData = classModel(**Data)
            session.add(newData)
            session.flush()
            session.commit()
            resIds.append(newData.id)
        # 将自增ID返回
        return {'id': resIds}
    except Exception as e:
        print(e)
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

# 删除数据方法
'''
支持多条数据删除，多条数据删除只需要传多个ID参数即可
单条示例 xxx/1
多条示例 xxx/1,2,3,4,5
返回结果为一个对象，包含俩数组
success 返回成功删除的的id序列
fail 返回删除失败的id序列
如果成功列表长度为 0 则返回参数错误
'''
def delete(className, oid):
    if not hasClass(className):
        return 404
        
    idArr = oid.split(',')
    succIds = []
    failIds = []
    
    try:
        classModel = getattr(model, className)
        for i in idArr:
            res = session.query(classModel).get(i)
            if res:
                session.delete(res)
                session.commit()
                succIds.append(i)
            else:
                failIds.append(i)
        if len(succIds) == 0:
            return 400
        else:
            return {'success': succIds, 'fail': failIds}
    except Exception as e:
        return 503
