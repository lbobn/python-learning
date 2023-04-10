"""
filter算子
过滤
"""

from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:\\Develop\\python\\python310\\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])

result_rdd = rdd.filter(lambda x: x % 2 == 0)

print(result_rdd.collect())
