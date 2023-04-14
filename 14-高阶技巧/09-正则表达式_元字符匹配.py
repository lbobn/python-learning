"""
元字符匹配
"""

# 匹配账号
import re

# 匹配账号,字母加数字,6-12位
username1 = "1234567"
username2 = "256ghg"
username3 = "adf"

r = r"[a-zA-Z0-9]{6,12}"  # r标记表示字符串内转义字符无效
print(re.findall(r, username1))
print(re.findall(r, username2))
print(re.findall(r, username3))

# 匹配QQ号 5-11位
r = r"[1-9]\d{4,10}"
print(re.findall(r, "282264656"))
print(re.findall(r, "082264656"))
print(re.findall(r, "0822"))

# 匹配邮箱号
r = r"^(\w+(\.\w+)*@(qq|QQ|163|gmail)(\.\w+)+)$"

print(re.findall(r, "13456.sb@qq.com"))
print(re.match(r, "cacac.aca.sb@163.com.cn").group())
print(re.findall(r, "134@qq.com"))
