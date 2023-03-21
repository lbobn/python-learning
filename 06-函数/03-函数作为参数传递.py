"""
匿名函数
函数作为参数
"""


def test_fun(compute):
    result = compute(1, 2)
    print(f"compute的类型是{type(compute)}")
    print(f"结果是:{result}")


def compute(x, y):
    return x + y


# 1.
test_fun(compute)

# 2. Lambda 匿名函数       lambda 传入参数: 函数体(一行)
test_fun(lambda x, y: x + y)
