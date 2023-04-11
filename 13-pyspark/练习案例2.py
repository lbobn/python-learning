"""
综合案例
1.各个城市名销售额排名,从大到小
2.全部城市,有哪些商品类别在售卖
3.北京市有哪些商品类别在售卖
"""

from pyspark import SparkConf, SparkContext
import os
import json

os.environ['PYSPARK_PYTHON'] = "D:/Develop/python/python310/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# TODO 需求一: 城市销售额排名
# 1.1 读取文件得到RDD
rdd = sc.textFile("D:/Test/python/python-learning/13-pyspark/data/orders.txt")

# 1.2 取出一个个JSON字符串

rdd_str_json = rdd.flatMap(lambda x: x.split("|"))
# print(rdd_str_json.collect())
# 1.3 将JSON字符串转为字典
rdd_dict = rdd_str_json.map(lambda x: json.loads(x))
# 1.4 取出城市和销售额数据
city_with_money_rdd = rdd_dict.map(lambda x: (x['areaName'], int(x['money'])))
# 1.5 按城市分组按销售额聚合
city_result_add = city_with_money_rdd.reduceByKey(lambda a, b: a + b)
# 1.6 按销售额聚合结果进行排序
result_rdd = city_result_add.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
print("需求1: ", result_rdd.collect())

# TODO 需求二: 全部城市有哪些商品类别在售卖
# 2.1 取出全部的商品类别
result_kind = rdd_dict.map(lambda x: x['category']).distinct()

# 2.2 对全部商品类别去重
print("需求2: ", result_kind.collect())

# TODO 需求三: 北京市有哪些商品类别在售卖
# 过滤出北京市数据
beijing_rdd = rdd_dict.filter(lambda x: x['areaName'] == "北京")
# 取出全部商品类别
result_beijing = beijing_rdd.map(lambda x: x['category']).distinct()
# 进行商品类别去重
print("需求3: ", result_beijing.collect())
