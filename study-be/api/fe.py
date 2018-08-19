# 引入 sanic 蓝图
from sanic import Blueprint
# 引入公共 RESTful 类
from core.app import listView, itemView
# 引入配置参数中的前缀参数
from config import PREFIX
from core import rest
from core.tool import ok, fail

# 配置蓝图
FIX = PREFIX['fe']
bp = Blueprint('fe', url_prefix=FIX)

# 加载默认 RESTful 接口生成路由
bp.add_route(listView.as_view(), '<name>')
bp.add_route(itemView.as_view(), '<name>/<oid>')

@bp.route('tree_channel', methods=['GET'])
async def tree_channel(request):
    sourceData = rest.getList({'pagesize': -1, 'sort': '-sort,-id'}, 'channel')
    if sourceData == 1:
        return fail('服务器内部错误', 500, 500)
    if sourceData['total'] < 1:
        return fail('您当前还没有添加任何栏目')

    sourceList = sourceData['list']

    def makeTree(pid, arr):
        res = []
        for i in arr:
            if i['pid'] == pid:
                rep = makeTree(i['id'], arr)
                if len(rep) != 0:
                    i['children'] = rep
                res.append(i)
        return res
    res = makeTree(0, sourceList)

    return ok(res)
