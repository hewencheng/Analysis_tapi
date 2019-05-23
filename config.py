import logging
import os

# if you use tornado project,this returns the root of the project
BASE_DIR = os.path.abspath(os.path.curdir)
app_version = '1.18.11.13.1'  # 项目版本号
debug_mode = True  # 是否是调试模式

big_file_path = '/data/asr-big-files'

settings = {
    "cookie_secret": "42233434",
    "debug": debug_mode,  # 非调试模式
}

HTTP_PORT = 8009  # 启动本app的端口

LOGGING_LEVEL = logging.DEBUG  # 日志输出的级别
LOGGING_STREAM = '/dev/stdout'  # 重定向到控制台

if __name__ == '__main__':
    # BASE_DIR = os.path.abspath('.')
    # print BASE_DIR
    pass
