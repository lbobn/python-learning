"""
list列表的常用
"""
my_list1 = ['张三', 23, '男']
# 查找下标索引
print(my_list1.index("男"))

# 修改指定下标值
my_list1[1] = 24
print(my_list1)

# 插入元素
my_list1.insert(1, "学生")
print(my_list1)

# 追加元素
my_list1.append(12345)
print(my_list1)
# 追加一批元素
my_list1.extend([9, 9, 9])
print(my_list1)

"""
元素的删除
"""
my_list2 = ['张三', 23, '男']

# del 列表[下标]
del my_list2[2]
print(my_list2)

# 列表.pop(下标)
pop = my_list2.pop(1)
print(f"删除{pop}后为{my_list2}")

# remove删除第一个匹配项
my_list3 = ['张三', '李四', '张三', '张三', '王五', '张三', '张三', ]
my_list3.remove('张三')
print(my_list3)

# 清空列表
my_list3.clear()
print(my_list3)

# 统计列表中某元素个数
my_list3 = ['张三', '李四', '张三', '张三', '王五', '张三', '张三', ]
count = my_list3.count("张三")
print(f"张三的个数{count}")

# 统计全部元素个数
i = len(my_list3)
print(f"列表{my_list3}的元素个数{i}")
