from bson import ObjectId

from dtlib.utils import list_have_none_mem
from dtlib.web.constcls import ConstData
from dtlib.web.tools import get_std_json_res

async def update_star(req, col):
    """
    修改备注,所有的都是能用的
    :return:
    """
    param_dict = req.get_post_body_dict()
    obj_id = param_dict.get('id', None)
    star = param_dict.get('star', None)
    print(obj_id)

    # if list_have_none_mem(*[obj_id, star]):
    #     return ConstData.msg_none

    res = await col.update_one({'_id': ObjectId(obj_id)}, {'$set': {'star':star}}, upsert=False)
    if res is None:
        return ConstData.msg_fail
    else:
        return ConstData.msg_succeed

async def update_remark(req, col):
    """
    修改备注,所有的都是能用的
    :return:
    """
    param_dict = req.get_post_body_dict()
    obj_id = param_dict.get('id', None)
    remark = param_dict.get('remark', None)
    print(obj_id)

    if list_have_none_mem(*[obj_id, remark]):
        return ConstData.msg_none

    res = await col.update_one({'_id': ObjectId(obj_id)}, {'$set': {'remark': remark}}, upsert=False)
    if res is None:
        return ConstData.msg_fail
    else:
        return ConstData.msg_succeed


async def update_remark_2(req, col):
    """
    语音修改备注
    :return:
    """
    param_dict = req.get_post_body_dict()
    obj_id = param_dict.get('id', None)
    remark = param_dict.get('remark', None)
    app_ver = param_dict.get('app_ver', None)
    cpu_type = param_dict.get('cpu_type', None)
    b_type = param_dict.get('b_type', None)
    b_plate = param_dict.get('b_plate', None)
    b_branch = param_dict.get('b_branch', None)
    bg_ver = param_dict.get('bg_ver', None)


    # if list_have_none_mem(*[obj_id, remark,app_ver,cpu_type,b_type,b_plate,b_branch,bg_ver]):
    #     return ConstData.msg_none

    res = await col.update_one({'_id': ObjectId(obj_id)}, {'$set': {'remark': remark,'cpu_type': cpu_type,'app_ver': app_ver,'b_type':b_type,
                                                                    'b_plate':b_plate,'b_branch':b_branch,'bg_ver':bg_ver}}, upsert=False)
    if res is None:
        return ConstData.msg_fail
    else:
        return ConstData.msg_succeed


async def get_doc_info(req, col):
    """
    根据id获取本记录的所有信息
    :param req: 
    :param col: 
    :return: 
    """
    obj_id = req.get_argument('id', None)

    if list_have_none_mem(*[obj_id, ]):
        return ConstData.msg_none

    res = await col.find_one({'_id': ObjectId(obj_id)})
    if res is None:
        return ConstData.msg_fail
    else:
        return get_std_json_res(data=res)
