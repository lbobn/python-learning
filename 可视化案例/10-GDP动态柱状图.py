"""
GDP动态图
"""

from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

f = open("D:\\Test\\python\\python-learning\\可视化案例\\1960-2019全球GDP数据.csv", "r", encoding="GB2312")
lines = f.readlines()

# 关闭文件
f.close()
# 删除第一行
lines.pop(0)

data_dict = {}

for line in lines:
    year = line.split(",")[0]
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])
    # 判断字典中是否含有key
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# print(data_dict)
# 创建时间线对象
time_line = Timeline({"theme": ThemeType.LIGHT})

# 排序年份
l = sorted(data_dict.keys())
for year in l:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出前八名
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1] / 100000000)

    # 构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()

    bar.set_global_opts(
        title_opts=TitleOpts(title=year + "年全球前八GDP")
    )

    time_line.add(bar, year)
#

time_line.add_schema(
    play_interval=500,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

time_line.render("1960-2019年全球GDP前8排名.html")
