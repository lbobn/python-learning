"""
通用功能
"""

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"value1": 1, "value2": 2, "value3": 3, "value4": 4, "value5": 5}

# len()元素个数

# max()最大元素
print(f"列表 最大的元素是:{max(my_list)}")
print(f"元组 最大的元素是:{max(my_tuple)}")
print(f"字符串 最大的元素是:{max(my_str)}")
print(f"集合 最大的元素是:{max(my_set)}")
print(f"字典 最大的元素是:{max(my_dict)}")
print("--------------------------------------------------")

# min()最小元素
print(f"列表 最小的元素是:{min(my_list)}")
print(f"元组 最小的元素是:{min(my_tuple)}")
print(f"字符串 最小的元素是:{min(my_str)}")
print(f"集合 最小的元素是:{min(my_set)}")
print(f"字典 最小的元素是:{min(my_dict)}")
print("--------------------------------------------------")

# 类型转换:容器转列表
print(f"列表转列表结果为:{list(my_list)}")
print(f"元组转列表结果为:{list(my_tuple)}")
print(f"字符串转列表结果为:{list(my_str)}")
print(f"集合转列表结果为:{list(my_set)}")
print(f"字典转列表结果为:{list(my_dict)}")
print("--------------------------------------------------")

# 类型转换:容器转元组
print(f"列表转元组结果为:{tuple(my_list)}")
print(f"元组转元组结果为:{tuple(my_tuple)}")
print(f"字符串转元组结果为:{tuple(my_str)}")
print(f"集合转元组结果为:{tuple(my_set)}")
print(f"字典转元组结果为:{tuple(my_dict)}")
print("--------------------------------------------------")

# 类型转换:容器转字符串
print(f"列表转字符串结果为:{str(my_list)}")  # "[1, 2, 3, 4, 5]"
print(f"元组转字符串结果为:{str(my_tuple)}")  # "(1, 2, 3, 4, 5)"
print(f"字符串转字符串结果为:{str(my_str)}")  # "abcdefg"
print(f"集合转字符串结果为:{str(my_set)}")  # "{1, 2, 3, 4, 5}"
print(f"字典转字符串结果为:{str(my_dict)}")  # "{'value1': 1, 'value2': 2, 'value3': 3, 'value4': 4, 'value5': 5}"
print("--------------------------------------------------")

# 类型转换:容器转集合
print(f"列表转集合结果为:{set(my_list)}")
print(f"元组转集合结果为:{set(my_tuple)}")
print(f"字符串转集合结果为:{set(my_str)}")
print(f"集合转集合结果为:{set(my_set)}")
print(f"字典转集合结果为:{set(my_dict)}")
print("--------------------------------------------------")

# sorted排序  放入list列表中
my_list = [3, 1, 5, 4, 2]
my_tuple = (3, 1, 5, 4, 2)
my_str = "bedcfga"
my_set = {3, 1, 5, 4, 2}
my_dict = {"value3": 1, "value1": 2, "value5": 3, "value4": 4, "value2": 5}

print(f"列表的排序结果是:{sorted(my_list)}")
print(f"元组的排序结果是:{sorted(my_list)}")
print(f"字符串的排序结果是:{sorted(my_list)}")
print(f"集合的排序结果是:{sorted(my_list)}")
print(f"字典的排序结果是:{sorted(my_list)}")

print(f"列表的反向排序结果是:{sorted(my_list, reverse=True)}")
print(f"元组的反向排序结果是:{sorted(my_list, reverse=True)}")
print(f"字符串的反向排序结果是:{sorted(my_list, reverse=True)}")
print(f"集合的反向排序结果是:{sorted(my_list, reverse=True)}")
print(f"字典的反向排序结果是:{sorted(my_list, reverse=True)}")
