class Student:
    name = None
    age = None
    gender = None
    nationality = None
    native_place = None

    def eat(self):
        print("吃饭")

    def say_hi(self):
        print("你好,我是" + self.name)


# 创建一个对象
stu = Student()
stu.name = "张三"
stu.age = 20
stu.gender = "男"
stu.nationality = "中国"
stu.native_place = "山东省"
stu.eat()

stu.say_hi()
print(stu.name, stu.age, stu.nationality)
