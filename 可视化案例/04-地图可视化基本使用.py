"""
地图
"""

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()

data = [
    ("北京市", 99),
    ("上海市", 88),
    ("湖南省", 818),
    ("广东省", 188),
    ("河南省", 288),
    ("福建省", 889),
    ("陕西省", 878)
]

# 添加数据
map.add("测试地图", data, "china")

# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
            {"min": 100, "max": 999, "label": "100-999", "color": "#990033"},
            {"min": 1000, "max": 9999, "label": "1000-9999", "color": "#CCFFFF"},
            {"min": 10000, "max": 99999, "label": "10000-99999", "color": "#CCFFFF"}
        ]
    )
)

# 绘图
map.render()
