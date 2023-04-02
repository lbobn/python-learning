"""
演示json数据和Python字典的转化
"""

import json
# 转为json    dumps
# 准备列表转为json
data = [{"name": "张三", "age": 11}, {"name": "李四", "age": 19}]
json_str = json.dumps(data, ensure_ascii=False)

print(type(json_str), " ", json_str)
# 准备字典转为json
d = {"name": "wangwu", "age": 10}
json_dumps = json.dumps(d)
print(type(json_dumps), " ", json_dumps)

# 转为Python      loads
# 将json转为Python数据类型
s = '[{"name": "张三", "age": 11}, {"name": "李四", "age": 19}]'
loads = json.loads(s)
print(type(loads), " ", loads)

s1 = '{"name": "wangwu", "age": 10}'
json_loads = json.loads(s1)
print(type(json_loads), " ", json_loads)
