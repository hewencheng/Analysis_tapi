"""
管理平台相应
"""
import math
import re
from apps.asr.utils import update_remark,update_star,get_doc_info,update_remark_2
from apps.base_server import MyBaseHandler

from dalib.db_cfg import col_movie_info,col_fish_data,col_music_soaring
from dtlib.aio.decos import my_async_paginator_motor,my_async_paginator_motor_7,my_async_paginator_motor100
from dtlib.web.decos import deco_jsonp
from dtlib.web.tools import get_std_json_res


class Update_movie_star(MyBaseHandler):
    @deco_jsonp(is_async=True)
    async def post(self):
        res = await update_star(self, col_movie_info)
        return res

class Get_movie_type(MyBaseHandler):
    @deco_jsonp(is_async=True)
    async def post(self):
        page_idx = self.get_argument('page_idx', '1')  # 页面索引号-var
        page_cap = self.get_argument('page_cap', '8')  # 一页的记录容量-var

        page_idx = int(page_idx)
        page_cap = int(page_cap)

        param_dict = self.get_post_body_dict()
        Type = param_dict.get('Type', None)
        filter = dict(Type=Type)
        page_count = await col_movie_info.count_documents(filter)
        msg_details = col_movie_info.find(filter,
                                             skip=(page_cap * (page_idx - 1)),
                                             limit=(page_cap)).sort('_id',1)  # 进行分页
        total_page = math.ceil(page_count / page_cap)  # 总的页面数
        msg_content_list = await msg_details.to_list(page_cap)
        detil_dict = dict(
            page_total_cnts=total_page,
            page_idx=page_idx,
            page_cap=page_cap,
            page_data=msg_content_list,
        )
        return get_std_json_res(data=detil_dict)


class Get_movie_list(MyBaseHandler):
    """
    折线图的分页
    """
    @deco_jsonp(is_async=True)
    @my_async_paginator_motor_7
    async def get(self):
        """
        :return:
        """
        Type = self.get_argument("Type", None)
        name = self.get_argument("name", None)
        # print(Type)
        # print(name)

        if Type == None :
            filter={}
        else:
            filter=dict(Type=Type)

        if name == None:
            filter2 = {}
        else:
            filter2 = dict(name=re.compile(name))
        if Type != None and name != None:
            filter3 = dict(Type=Type,name=re.compile(name))
        else:
            filter3={}

        return col_movie_info,filter,filter2,filter3


class Get_fishdata_list(MyBaseHandler):
    """
    折线图的分页
    """
    @deco_jsonp(is_async=True)
    @my_async_paginator_motor
    async def get(self):
        """
        :return:
        """
        return col_fish_data, {}


class Get_misic_soaring_list(MyBaseHandler):
    """
    折线图的分页
    """
    @deco_jsonp(is_async=True)
    @my_async_paginator_motor
    async def get(self):
        """
        :return:
        """
        return col_music_soaring, {}


class Get_score_list(MyBaseHandler):
    """
    平分统计折线图
    """

    @deco_jsonp(is_async=True)
    async def get(self):
        """
        :return:
        """
        filter =dict(star=True)
        a_count = await col_movie_info.count_documents(filter)
        fun_list = await col_movie_info.find(filter).to_list(a_count)
        res_list = []
        for val in fun_list:
            res_list.append([val['score'],
                             val['name'],
                             val['rank'],
                             val['quote']])
        score = []
        for res in fun_list:
            score.append(float(res['score']))
        score_max = max(score)
        score_min = min(score)
        score_value = {"score_max": score_max, "score_min": score_min}

        typelist = ["犯罪","剧情","爱情","喜剧","动画","纪录片","传记","动作","奇幻","儿童","悬疑","冒险","科幻",]
        a_countlist = []
        for val in typelist:
            filter = dict(Type=val,star=True)
            a_count = await col_movie_info.count_documents(filter)
            a_countlist.append(a_count)
        filter = dict(star=True)
        type_total = await col_movie_info.count_documents(filter)

        res_dict = dict(res_list=res_list,
                        score_value=score_value,
                        typelist=typelist,
                        a_countlist=a_countlist,
                        type_total=type_total)

        return get_std_json_res(data=res_dict)


class Get_fishstatistics_list(MyBaseHandler):
    """
    斗鱼折线图的分页
    """
    @deco_jsonp(is_async=True)
    @my_async_paginator_motor100
    async def get(self):
        """
        :return:
        """
        return col_fish_data, {}



