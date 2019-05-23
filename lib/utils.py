# 获取文件的md5值
import hashlib
from os import path

from tabulate import tabulate

import config
from dtlib.dtlog import dlog


def md5file(file_path):
    f = open(file_path, 'rb')
    md5obj = hashlib.md5()
    md5obj.update(f.read())
    hash_res = md5obj.hexdigest()
    f.close()
    return str(hash_res).lower()


def get_file_size(file_path):
    """
    获取文件的大小,结果保留两位小数，单位为MB
    :param file_path:
    :return:
    """
    fsize = path.getsize(file_path)
    fsize = fsize / float(1024 * 1024)
    return round(fsize, 4)


def output_server_info(**kwargs):
    """
    输出服务器相关配置信息
    :param kwargs:
    :return:
    """

    port = kwargs.get('port', 0)

    tbl_out = tabulate([
        ['http_port', port],
        ['app_ver', config.app_version]
    ],
        tablefmt='grid')
    print(tbl_out)
    print('http://127.0.0.1:%s' % port)


def output_urls(urls):
    """
    输出所有的url
    :return:
    """
    dlog.debug(len(urls))
    for item in urls:
        print(item)
