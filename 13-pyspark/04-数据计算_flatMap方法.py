"""
flatMap算子
对结果解除嵌套
"""
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:\\Develop\\python\\python310\\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)
rdd = sc.parallelize(["nihao666 hello world", "hahaha hi hello", "nice to meet you"])

rdd2 = rdd.flatMap(lambda x: x.split())

print(rdd2.collect())

sc.stop()
