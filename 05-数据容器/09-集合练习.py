"""
练习集合
    list->set
"""

l = ["hello", "it", "world", 666, "hello", "world", "zhangsan"]

s = set()

for element in l:
    s.add(element)

print(s)
