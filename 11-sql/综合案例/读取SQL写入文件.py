"""
读取SQL数据写入文件
"""

from pymysql import Connection
import json

conn = Connection(host="localhost", port=3306, user="root", password="25gn3umb")
cursor = conn.cursor()
conn.select_db("py_sql")
cursor.execute("select * from orders;")

fetchall = cursor.fetchall()

f = open("text.txt", "a", encoding="UTF-8")

for r in fetchall:
    # print(type(r[0]))
    # print(r[3])
    data_dict = {"date": str(r[0]), "order_id": r[1], "money": r[2], "province": r[3]}
    # print(data_dict)
    data_json = json.dumps(data_dict, ensure_ascii=False)  # ensure_ascii为False可返回包含非ASCII值
    f.write(data_json)
    f.write("\n")

f.close()
conn.close()
