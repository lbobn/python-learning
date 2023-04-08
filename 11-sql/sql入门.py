"""
sql入门
"""

from pymysql import Connection

conn = Connection(host="localhost", port=3306, user="root", password="25gn3umb")

# print(conn.get_server_info())

conn.select_db("spj")
# 执行SQL
cursor = conn.cursor()  # 获取游标对象
cursor.execute("select * from spj")

fetchall = cursor.fetchall()

for r in fetchall:
    print(r)

conn.close()
