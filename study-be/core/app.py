from sanic import Sanic
from sanic.views import HTTPMethodView
from core.process import doProcess
from core.tool import fail, query2Dict
# 使用 pkgutil 模块实现动态加载
import pkgutil

app = Sanic(__name__)

# 在服务启动之前执行
@app.listener('before_server_start')
async def registerModule(app, loop):
    r = 'process'
    app.process = {}
    # 进行第一层循环，加载不同接口前缀对应的模块
    for x, n, _ in pkgutil.iter_modules([r]):
        m = x.find_module(r + '.' + n).load_module(r + '.' + n)
        # 进行第二层循环，加载对应的不同前后处理模块
        for xx, nn, __ in pkgutil.iter_modules([r + '/' + n]):
            mm = xx.find_module(r + '.' + n + '.' + nn).\
                    load_module(r + '.' + n + '.' + nn)
            # 进行第三层循环，加载前后处理的所有响应模块
            for xxx, nnn, ___ in pkgutil.iter_modules([r + '/' + n + '/' + nn]):
                mmm = xxx.find_module(r + '.' + n + '.' + nn + '.' + nnn).\
                        load_module(r + '.' + n + '.' + nn + '.' + nnn)
                # 将得到的结果装载到 app.process 以供全局使用
                app.process[n+nn+nnn] = mmm


# restFul 方法列表公用类
class listView(HTTPMethodView):
    async def get(self, request, name):
        query = query2Dict(request.query_string)
        return await doProcess(app, name, request, query, 'ls')
    async def post(self, request, name):
        data = request.json
        if data:
            if 'batch_additon' in data \
                    and isinstance(data['batch_additon'], list):
                data = {'data': data['batch_additon']}
            else:
                data = {'data': [data]}
            return await doProcess(app, name, request, data, 'post')
        else:
            return fail('数据不能为空', 400)

# restFul 方法内容公用类
class itemView(HTTPMethodView):
    async def get(self, request, name, oid):
        query = query2Dict(request.query_string)
        return await doProcess(app, name, request, query, 'get', oid)
    async def put(self, request, name, oid):
        data = request.json
        if data:
            return await doProcess(app, name, request, data, 'put', oid)
        else:
            return fail('数据不能为空', 400)
    async def delete(self, request, name, oid):
        query = query2Dict(request.query_string)
        return await doProcess(app, name, request, query, 'delete', oid)

