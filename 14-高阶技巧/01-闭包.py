"""
闭包
"""


def outer(logo):
    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")

    return inner


f1 = outer("nihao")
f1("大家好")


def creat_account(balance=0):
    def ATM(money, deposit=True):
        nonlocal balance  # 声明全局变量
        if deposit:
            balance += money
            print(f"存钱:{money} 余额:{balance}")
        else:
            balance -= money
            print(f"存钱:{money} 余额:{balance}")

    return ATM


ATM = creat_account()
ATM(10, deposit=True)
ATM(5, deposit=False)
