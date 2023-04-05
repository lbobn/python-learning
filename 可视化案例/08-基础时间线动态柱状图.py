"""
时间线动态图
"""

from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "日本"])
bar1.add_yaxis("GDP", [30, 20, 10])
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "日本"])
bar2.add_yaxis("GDP", [40, 30, 20])
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "日本"])
bar3.add_yaxis("GDP", [60, 50, 46])
bar3.reversal_axis()

time_line = Timeline(
    {"theme": ThemeType.LIGHT}  # 设置主题
)

time_line.add(bar1, "点1")
time_line.add(bar2, "点2")
time_line.add(bar3, "点3")

time_line.add_schema(
    play_interval=500,  # 自动播放时间间隔
    is_timeline_show=True,  # 是否展示时间线
    is_auto_play=True,  # 是否自动播放
    is_loop_play=True  # 是否循环播放
)

time_line.render("基础时间线动态柱状图.html")
