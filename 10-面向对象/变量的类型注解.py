"""
类型注解
"""

name: str = "张三"
age: int = 19
is_boy: bool = True

l: list = [1, 2, 3]
t: tuple = (1, "nihao", True)
s: set = {2, 5, 6, 54}
d: dict = {"zhangsan": 23, "lisi": 25}

l2: list[int] = [1, 2, 3]
t2: tuple[int, str, bool] = (1, "nihao", True)
s2: set[int] = {2, 5, 6, 54}
d2: dict[str, int] = {"zhangsan": 23, "lisi": 25}
