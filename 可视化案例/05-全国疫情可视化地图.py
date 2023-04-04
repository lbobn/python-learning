"""
全国疫情可视化地图
"""

import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

f = open("D:\Test\python\python-learning\可视化案例\疫情.txt", "r", encoding="UTF-8")
data = f.read()

# 关闭文件
f.close()

# 取到各省数据
# 将字符串JSON转为Python字典
data_dict = json.loads(data)
# 从字典中取到各省数据
province_data_list = data_dict["areaTree"][0]["children"]
# 组装每个省份和确诊人数为元组,将其分装为列表
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]  # 省份名称
    if province_name == "北京":
        province_name = "北京市"
    elif province_name == "上海":
        province_name = "上海市"
    elif province_name == "重庆":
        province_name = "重庆市"
    elif province_name == "天津":
        province_name = "天津市"
    elif province_name == "香港":
        province_name = "香港特别行政区"
    elif province_name == "澳门":
        province_name = "澳门特别行政区"
    elif province_name == "宁夏":
        province_name = "宁夏回族自治区"
    elif province_name == "新疆":
        province_name = "新疆维吾尔自治区"
    elif province_name == "西藏":
        province_name = "西藏自治区"
    elif province_name == "内蒙古":
        province_name = "内蒙古自治区"
    elif province_name == "广西":
        province_name = "广西壮族自治区"
    else:
        province_name = province_name + "省"

    province_confirm = province_data["total"]["confirm"]  # 确诊人数
    data_list.append((province_name, province_confirm))

print(data_list)
# 创建地图对象

map = Map()

map.add("各省确诊人数", data_list, "china")

# 设置全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min": 1, "max": 99, "label": "1~99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100~999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000~4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000~9999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000~99999人", "color": "#CC3333"},
            {"min": 100000, "label": "100000人以上", "color": "#990033"},
        ]
    )
)
# 绘图
map.render("全国疫情地图.html")
