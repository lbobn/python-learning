"""
PySpark入口对象
"""

"""
SparkContext类对象,是PySpark编程中一切功能的入口
"""
# 导包
from pyspark import SparkConf, SparkContext

# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 基于SparkConf创建SparkContext对象
sc = SparkContext(conf=conf)

# 打印PySpark运行版本
print(sc.version)
# 停止SparkContext对象运行
sc.stop()
