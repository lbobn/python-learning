"""
猜数字,无限次机会
"""
import random

r = random.randint(1, 100)

flag = True
while flag:
    guess_num = int(input("请输入要猜的数字"))
    if guess_num == r:
        print("猜对了")
        flag = False
    else:
        if guess_num > r:
            print("猜大了")
        else:
            print("猜小了")

