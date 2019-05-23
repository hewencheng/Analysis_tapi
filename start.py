"""
可以使用tornado server
"""
import argparse
import logging

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from apps.base_server import MyApplication
from config import HTTP_PORT, settings, LOGGING_LEVEL, BASE_DIR
from dtlib.dtlog import dlog
from dtlib.tornado.tools import get_apps_url
from dtlib.tornado.utils import output_sys_info
from lib.utils import output_server_info

if __name__ == '__main__':
    # 设置日志输出级别
    dlog.setLevel(LOGGING_LEVEL)
    logging.getLogger('asyncio').setLevel(logging.WARNING)

    parser = argparse.ArgumentParser()
    parser.add_argument('--port', help='port of http server', default=HTTP_PORT)
    args = parser.parse_args()
    print(args.port)

    urls = get_apps_url(BASE_DIR)

    app = MyApplication(
        urls,
        **settings
    )

    server = HTTPServer(
        app,
        xheaders=True  # when running behind a load balancer like nginx
    )
    server.bind(args.port)  # 设置端口
    server.start(num_processes=1)

    # 输出运行服务的相关信息
    output_sys_info()
    output_server_info(port=args.port)
    # output_urls(urls)

    IOLoop.current().start()
