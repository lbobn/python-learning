"""
list列表的定义
"""

# 定义一个list列表
my_list = ["张三", "李四", "王五"]
# print(my_list)
# print(type(my_list))
# 元素的数据类型无限制
my_list = ["张三", 666, True]
# print(my_list)
# print(type(my_list))

# 定义一个嵌套列表
my_list = [[1, 2, 3], [4, 5, 6]]
# print(my_list)
# print(type(my_list))

# 正向索引
print(my_list[0])
# 逆向索引 从右向左 -1~-n
print(my_list[-1])
# 嵌套列表
print(my_list[0][1])
