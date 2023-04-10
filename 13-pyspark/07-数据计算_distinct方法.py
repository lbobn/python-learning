"""
distinct算子:数据去重
"""
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:/Develop/python/python310/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 4, 2, 1, 3, 4, 6, 3, 1, 2])
rdd_distinct = rdd.distinct()
print(rdd_distinct.collect())
