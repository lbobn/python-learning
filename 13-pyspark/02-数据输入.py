"""
数据输入
获得RDD对象
    RDD:分布式弹性数据集
"""

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 1 通过parallelize()方法将Python对象加载到Spark内,成为RDD对象
rdd1 = sc.parallelize([1, 2, 3, 4, 5])
# rdd2 = sc.parallelize((1, 2, 3, 4, 5))
# rdd3 = sc.parallelize({1, 2, 3, 4, 5})
# rdd4 = sc.parallelize("abcdefg")
# rdd5 = sc.parallelize({"key1": "value1", "key2": "value2"})
#
print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# print(rdd4.collect())
# print(rdd5.collect())

# 2 通过textFile方法,读取文件数据加载为RDD对象
add = sc.textFile("text.txt")
print(add.collect())

sc.stop()
