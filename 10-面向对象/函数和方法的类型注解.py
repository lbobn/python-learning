"""
函数和方法的类型注解
"""

"""
类型注解为提示性,不按照注解传参不会报错
"""


def add(x: int, y: int):
    # 形参注解
    return x + y


def func1(data: list):
    # 形参注解
    pass


def func2(data: list) -> list:
    # 返回值注解
    return data


print(add(5, 8))

func1([1, 2])

print(func2([1, 2]))

"""
union类型
"""

from typing import Union

l: list[Union[int, str]] = [1, 2, "nihao", "hello"]


def func(data: Union[str, int]) -> Union[str, int]:
    pass


func(12)
