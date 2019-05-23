import dtlib
from apps.base_server import MyBaseHandler
from config import app_version
from dtlib import timetool
from dtlib.web.decos import deco_jsonp
from dtlib.web.tools import get_std_json_res


class MainHandler(MyBaseHandler):
    def get(self):
        self.redirect('/web/')


class AppInfo(MyBaseHandler):
    """
    获取本web应用的基本信息
    """

    @deco_jsonp(is_async=False)
    def get(self):
        res = dict(
            server='tornado',  # web服务器
            dtlib_version=dtlib.VERSION,  # 第三方库dt-lib的版本
            req_time=timetool.get_current_time_string(),  # 当前查询时间点
        )
        return get_std_json_res(data=res)
