"""
集合:不支持重复,内容无序

不支持下标索引访问
"""

"""
列表:[]
元组:()
字符串:""
集合:{}
"""

# 定义
set1 = {"123", "hello", "zhangsan", "zhangsan"}  # 去重
set2 = set()  # 空集合
print(set1)  # {'123', 'zhangsan', 'hello'}
print(set2)  # set()

# 添加新元素
set1.add("world")
set1.add("hello")  # 去重
print(set1)  # {'123', 'zhangsan', 'hello', 'world'}

# 移除元素
set1.remove("zhangsan")
print(set1)  # {'hello', 'world', '123'}

# 随机取出元素  元素被移除
set3 = {"123", "hello", "zhangsan"}
pop = set3.pop()
print(f"set3去除随机元素{pop}后为{set3}")

# 清空集合
set4 = {"123", "hello", "zhangsan"}
set4.clear()
print(set4)  # set()

# 取出两个集合的差集
# 在集合2中没有的集合1的元素
set5 = {1, 2, 3}
set6 = {1, 5, 6}
print(f"取出{set5}和{set6}的差集为{set5.difference(set6)}")

# 消除两个集合的差集
set7 = {1, 2, 3}
set8 = {1, 5, 6}
set7.difference_update(set8)
print(f"消除{set5}和{set6}的差集后,集合1为{set7}")

# 2个集合合并为一个  原集合不变
set9 = {1, 2, 3}
set10 = {1, 5, 6}
union = set9.union(set10)
print(f"合并后为{union}")  # {1, 2, 3, 5, 6}

# 统计集合元素数量
set11 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
num = len(set11)
print(num)

# 集合遍历
for element in set11:
    print(element, " ", end='')
