# 引入 sanic 蓝图
from sanic import Blueprint
# 引入公共 RESTful 类
from core.app import listView, itemView
# 引入配置参数中的前缀参数
from config import PREFIX

# 配置蓝图
FIX = PREFIX['fe']
bp = Blueprint('fe', url_prefix=FIX)

# 加载默认 RESTful 接口生成路由
bp.add_route(listView.as_view(), '<name>')
bp.add_route(itemView.as_view(), '<name>/<oid>')
