from tornado.web import Application
from dtlib.tornado.base_hanlder import MyOriginBaseHandler

# from dtlib.web.valuedict import ValueDict
# commentKeep_ValueDict = ValueDict(0, '')
# commentKeep_WebToken = WebToken()


class MyApplication(Application):
    """
    加入一些自定义的应用
    """

    def set_async_mongo(self, mdb):
        """
        异步的mongo连接池
        :param async_mongo_pool:
        :return:
        """
        # self.settings[db_key] = async_mongo_pool
        self.db = mdb


class MyBaseHandler(MyOriginBaseHandler):
    """
    自定义session的类,基于tornado的

    - logsession是登录的token,使用mongodb来存储
    - sessionid使用redis来存储,以后用token,不用session了

    """

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers",
                        "x-requested-with,access_token")  # 这里要填写上请求带过来的Access-Control-Allow-Headers参数，如access_token就是我请求带过来的参数
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS, DELETE");  # 请求允许的方法
        self.set_header("Access-Control-Max-Age", "3600") # 用来指定本次预检请求的有效期，单位为秒，，在此期间不用发出另一条预检请求。
        # 定义一个响应OPTIONS 请求，不用作任务处理
    def options(self):
        pass

    # def set_default_headers(self):
    #     self.set_header('Access-Control-Allow-Origin', '*')
    #     self.set_header('Access-Control-Allow-Headers', '*')
    #     self.set_header('Access-Control-Max-Age', 3600)
    #     self.set_header('Content-type', 'application/json')
    #     self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    #     self.set_header('Access-Control-Allow-Headers',  # '*')
    #                     'authorization, Authorization, Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')



    def __init__(self, *args, **kwargs):
        super(MyBaseHandler, self).__init__(*args, **kwargs)




