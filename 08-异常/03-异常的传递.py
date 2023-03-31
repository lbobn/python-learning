"""
异常传递
"""


# 定义出异常的方法
def func1():
    print("func1开始执行")
    numbers = 1 / 0
    print("func1结束执行")


# 定义无异常的方法
def func2():
    print("func2开始执行")
    func1()
    print("func2结束执行")


# 定义方法调用上面方法
def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常{e}")


main()
