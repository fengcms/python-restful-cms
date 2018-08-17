from sanic import Sanic
from sanic.views import HTTPMethodView
from core.process import doProcess
from core.tool import fail, query2Dict

# restFul 方法列表公用类
class listView(HTTPMethodView):
    async def get(self, request, name):
        query = query2Dict(request.query_string)
        print(request.query_string)
        print(query)
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

app = Sanic(__name__)
