"""
省级地图
"""

# 读取文件
import json
from pyecharts.charts import Map
from pyecharts.options import *

f = open("D:\Test\python\python-learning\可视化案例\疫情.txt", "r", encoding="UTF-8")
data = f.read()
# 关闭文件
f.close()

# 取出湖北省数据
data_dict = json.loads(data)
cities_data = data_dict["areaTree"][0]["children"][6]["children"]

# 准备数据为元组并放入list
data_list = []
for city_data in cities_data:
    city_name = city_data["name"]
    if city_name == "恩施州":
        city_name = "恩施土家族苗族自治州"
    elif city_name == "神农架":
        city_name = "神农架林区"
    else:
        city_name = city_name + "市"
    city_confirm = city_data["total"]["confirm"]
    data_list.append((city_name, city_confirm))

print(data_list)
# 构建地图
map = Map()
map.add("湖北省疫情地图", data_list, "湖北")

# 设置全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="湖北疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
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

map.render("湖北疫情地图.html")
