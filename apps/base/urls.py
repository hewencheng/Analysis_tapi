from apps.base.handlers import *
from dtlib import filetool

app_path = filetool.get_parent_folder_name(__file__)  # set the relative path in one place

url = [

    # 公用
    (r"/", MainHandler),
    (r"/app-info/", AppInfo),
]
