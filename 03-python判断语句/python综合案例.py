"""
猜数字小游戏
"""
import random

r = random.randint(1, 10)

guess_number = int(input("请输入你要猜的数字"))

if guess_number == r:
    print("恭喜你,猜中了")
else:
    if guess_number > r:
        print("猜大了")
    else:
        print("猜小了")
    guess_number = int(input("请输入你要猜的数字"))
    if guess_number == r:
        print("恭喜你,猜中了")
    else:
        if guess_number > r:
            print("猜大了")
        else:
            print("猜小了")

        guess_number = int(input("请输入你要猜的数字"))

        if guess_number == r:
            print("恭喜你,猜中了")
        else:
            print(f"三次都猜错了,正确答案为{guess_number}")
