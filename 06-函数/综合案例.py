"""
ATM
"""
money = 5000000
name = None

name = input("请输入您的姓名")


def query(flag):
    """
    查询余额
    :return:
    """
    if flag:
        print("--------------查询余额--------------")
    print(f"余额还剩{money}")


def save(value):
    """
    存款
    :param value: 存款数目
    :return:
    """
    print("--------------存款--------------")
    global money
    money += value
    query(False)


def get(value):
    """
    取款
    :param value:
    :return:
    """
    print("--------------取款--------------")
    global money
    if money < value:
        print("余额不足")
        return None
    money -= value
    query(False)


def menu():
    print("--------------主菜单--------------")
    print(f"{name},您好,欢迎使用ATM,请选择:")
    print("\t1.查询余额")
    print("\t2.存款")
    print("\t3.取款")
    print("\t0.退出")
    return input("请输入您的选择:")


#
while True:
    s = menu()
    if s == "1":
        query(True)
        continue
    elif s == "2":
        num = int(input("您想存入多少钱:"))
        save(num)
        continue
    elif s == "3":
        num = int(input("您想取多少钱:"))
        get(num)
        continue
    else:
        print("程序退出")
        break
