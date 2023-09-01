"""
魔术方法
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student类对象, name={self.name}, age={self.age}"

    # __lt__   小于或大于的比较
    def __lt__(self, other):
        return self.age < other.age

    # __le__   小于等于或大于等于的比较
    def __le__(self, other):
        return self.age <= other.age

    # __eq__  等于的比较
    def __eq__(self, other):
        return self.age == other.age


student1 = Student("李四", 11)
student2 = Student("王五", 15)
print(student1)
print(str(student1))

print(student1 > student2)
print(student1 < student2)

print(student1 <= student2)
print(student1 >= student2)

print(student1 == student2)  # ==号默认比较地址值
