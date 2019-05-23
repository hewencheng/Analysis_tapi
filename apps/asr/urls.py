from apps.asr.handlers import *
from dtlib import filetool

app_path = filetool.get_parent_folder_name(__file__)  # 'apis'  # set the relative path in one place
print(app_path)
url = [
    (r"/%s/get_movie_report_list/" % app_path, Get_movie_list),  # 电影
    (r"/%s/update_movie_report_star/" % app_path, Update_movie_star),  # 选择
    (r"/%s/get_score_report_list/" % app_path, Get_score_list),  # 电影平分
    (r"/%s/get_movie_type_list/" % app_path, Get_movie_type),  # 搜索
    (r"/%s/get_music_soaring_report_list/" % app_path, Get_misic_soaring_list),  # 飙升音乐
    (r"/%s/get_fishdata_report_list/" % app_path, Get_fishdata_list),  # 主播信息
    (r"/%s/get_fish_statistics_list/" % app_path, Get_fishstatistics_list),  # 主播信息
]
