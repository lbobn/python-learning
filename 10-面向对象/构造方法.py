"""
构造方法
"""


class Student:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个对象")


stu1 = Student("zhangsan", 20, "13125623256")

print(f"stu1:name={stu1.name},age={stu1.age},tel={stu1.tel}")
