"""
多态
"""


class Animal:
    def speak(self):
        pass


class Cat(Animal):
    def speak(self):
        print("喵喵叫")


class Dog(Animal):
    def speak(self):
        print("汪汪叫")


def make_noice(animal: Animal):
    animal.speak()


cat = Cat()
dog = Dog()

make_noice(cat)
make_noice(dog)
