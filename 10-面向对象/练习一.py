"""
学生信息录入
"""


class Student:
    name = None
    age = None
    address = None

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


for i in range(1, 11):
    print(f"当前录入第{i}位学生信息,总共需要输入10位学生信息")
    name = input("请输入学生姓名:")
    age = input("请输入学生年龄:")
    address = input("请输入学生地址:")
    stu = Student(name, age, address)
    print(f"第一位学生信息录入完成,信息为:[学生年龄: {stu.name}, 年龄: {stu.age}, 地址: {stu.address}]")
