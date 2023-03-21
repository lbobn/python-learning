"""
函数的多种传入和使用
"""


def user_info(name, age, gender):
    print(f"姓名是:{name},年龄是:{age},性别是:{gender}")


# 位置参数
user_info("小明", 20, "男")

# 关键字参数
user_info(name="小王", age=23, gender="男")
user_info(gender="女", age=18, name="潇潇")
user_info("小丽", age=18, gender="女")


# 缺省参数
def user_info(name, age, gender="男"):
    print(f"姓名是:{name},年龄是:{age},性别是:{gender}")


user_info('小天', 14)
user_info("小天", 12, "女")


# 不定长 - 位置不定长  *号
def user_info(*args):
    print(f"args的类型:{type(args)},内容为:{args}")


user_info(1, 2, 3, "dwc", True)


# 不定长 - 关键字不定长   **号
def user_info(**kwargs):
    print(f"kwargs的类型:{type(kwargs)},内容为:{kwargs}")


user_info(name="张三", age=23, gender="男")
