"""
工厂模式
便于创建大量对象
"""


class Person:
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


class Worker(Person):
    pass


class PersonFactory:

    def getPerson(self, p_type):
        if p_type == 'w':
            return Worker()
        elif p_type == 't':
            return Teacher()
        else:
            return Student()


pf = PersonFactory()
worker = pf.getPerson("w")
teacher = pf.getPerson("t")
student = pf.getPerson("s")
