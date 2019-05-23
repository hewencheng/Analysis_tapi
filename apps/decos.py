from __future__ import division

import functools
import os
import traceback


# from apps.account.docs import WebToken, AccessToken
# from apps.webapp.docs import AppSession


def get_callback_result(callback, res_str):
    """
    根据callback后的jsonp语句
    :param callback:
    :param res_str:
    :return:
    """
    if callback is None:
        return res_str
    else:
        return '%s(%s)' % (callback.encode("utf-8"), res_str)


def wrap_track_back(method):
    """
    打印出异常信息
    :param method:
    :return:
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        try:
            return method(self, *args, **kwargs)
        except Exception as e:
            traceback.print_exc()
            return

    return wrapper


if __name__ == '__main__':
    print(os.path.dirname(__file__))
    print(os.path.abspath('.'))
