"""
装饰器
    在不破坏原有函数同时加入新功能
"""


# 一般写法
# def sleep():
#     import random
#     import time
#     print("睡觉中")
#     time.sleep(random.randint(1, 9))
#
# def outer(func):
#
#     def inner():
#         print("我睡觉了")
#         func()
#         print("我睡醒了")
#     return inner
#
# f = outer(sleep)
# f()


# 改善
def outer(func):
    def inner():
        print("我睡觉了")
        func()
        print("我睡醒了")

    return inner


@outer
def sleep():
    import random
    import time
    print("睡觉中")
    time.sleep(random.randint(1, 9))


sleep()
