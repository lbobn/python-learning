"""
字典的常用操作

"""
d1 = {"张三": 77, "李四": 88, "王五": 22}
print(d1)
# 新增元素
d1["李信"] = 55
print("新增后", d1)

# 元素更新
d1["张三"] = 100
print("更新后", d1)

# 删除元素
pop = d1.pop("张三")
print(f"删除的元素张三分数{pop}后为{d1}")

# 清空元素
d1.clear()
print(f"清空后为{d1}")

# 获取全部key
d2 = {"张三": 77, "李四": 88, "王五": 22}
keys = d2.keys()
print(f"字典{d2}的全部key为{keys}")

# 遍历字典

# 方式一:获取全部key来遍历
print("方式一")
for key in keys:
    print(f"字典的key为{key}")
    print(f"字典的key{key}的value为{d2[key]}")
# 方式二:直接对字典for循环,直接得到key
print("方式二")
for key in d2:
    print(f"字典的key为{key}")
    print(f"字典的key{key}的value为{d2[key]}")

# 统计字典的元素数量
len = len(d2)
print(f"字典{d2}的元素个数{len}")
