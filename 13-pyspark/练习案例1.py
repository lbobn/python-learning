"""
单词个数统计
"""

# 构建执行入口对象
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:\\Develop\\python\\python310\\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 读取文件数据
rdd = sc.textFile("words.txt")
# print(rdd.collect())
# 取出全部单词
word_rdd = rdd.flatMap(lambda x: x.split(" "))
# 将所有单词转换为二元元组
word_with_one_rdd = word_rdd.map(lambda x: (x, 1))
# 分组求和
result_rdd = word_with_one_rdd.reduceByKey(lambda a, b: a + b)
# 打印结果
print(result_rdd.collect())
