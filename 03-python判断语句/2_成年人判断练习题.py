# 获取输入
# age = int(input("请输入你的年龄"))

# if判断
# if age >= 18:
#     print("您已成年,需要补票10元")
#
# print("祝您游玩愉快")

# height = int(input("请输入身高"))
#
# if height >= 120:
#     print("身高大于120,请补票")
# else:
#     print("身高不大于120,免费游玩")

height = int(input("请输入身高"))
VIP_level = int(input("请输入VIP等级"))
if height < 120:
    print("身高小于120,可免费游玩")
elif VIP_level > 3:
    print("您的VIP等级大于3,可免费游玩")
else:
    print("您需要购票游玩")

print("游玩愉快")
