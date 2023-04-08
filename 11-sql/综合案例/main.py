"""
数据可视化
"""

from file_define import TextFileReader, JSONFileReader
from data_define import Record
from pymysql import Connection

text_file_reader = TextFileReader("D:\\Test\\python\\python-learning\\10-面向对象\\数据分析案例\\2011年1月销售数据.txt")
json_file_reader = JSONFileReader("D:\\Test\\python\\python-learning\\10-面向对象\\数据分析案例\\2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 将两个月份合二为一
all_data: list[Record] = jan_data + feb_data

# for i in all_data:
#     print(i)

# 构建mysql连接对象
conn = Connection(host="localhost", port=3306, user="root", password="25gn3umb", autocommit=True)

# 获得游标对象
cursor = conn.cursor()

conn.select_db("py_sql")

for record in all_data:
    sql = f"insert into orders(order_date, order_id, money, province) " \
          f"values('{record.date}','{record.order_id}', {record.money}, '{record.province}')"
    # print(sql)
    cursor.execute(sql)

conn.close()
