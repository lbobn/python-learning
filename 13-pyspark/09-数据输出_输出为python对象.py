"""
RDD输出为python对象
"""

from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:/Develop/python/python310/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

#
rdd = sc.parallelize([1, 2, 3, 4, 5])

# collect算子,输出为list
rdd_list = rdd.collect()
print(rdd_list)

# reduce
rdd_reduce = rdd.reduce(lambda a, b: a + b)
print(rdd_reduce)

# take
rdd_take = rdd.take(3)
print(rdd_take)

# count
count = rdd.count()
print(count)
