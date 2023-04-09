"""
map算子
接收处理函数,可用Lambda表达式快速编写
对RDD内的元素逐个处理,返回一个新RDD
"""

from pyspark import SparkConf, SparkContext

import os

os.environ['PYSPARK_PYTHON'] = "D:\\Develop\\python\\python310\\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])


def func(data):
    return data * 10


# rdd2 = rdd.map(func)

rdd2 = rdd.map(lambda x: x * 10).map(lambda x: x + 5)
print(rdd2.collect())

sc.stop()
