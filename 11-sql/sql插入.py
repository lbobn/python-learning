"""
插入数据
"""

from pymysql import Connection

conn = Connection(host="localhost", port=3306, user="root", password="25gn3umb", autocommit=True)  # 自动确认(事务)

conn.select_db("xskk")

cursor = conn.cursor()
cursor.execute("insert into student values('123', 'luyu', 23, 'IS')")

conn.commit()

conn.close()
