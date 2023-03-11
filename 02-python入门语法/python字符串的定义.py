# 单引号定义法
str1 = '张三'
str2 = "李四"
str3 = """
你
好
"""

name = '"你好"'
name1 = "'你好'"
name2 = "\'你好\'"

# 字符串格式化
# 格式:"%占位符"%变量
name3 = "你好呀"
message = "你也好"
class_number = 19

print("hello %s,%s,我%s岁了" % (name3, message, class_number))

# 快速格式化
# 字符串前+f        f:format
stu_name = "张三"
sex = "男"
age = 19
print(f"姓名:{stu_name}, 性别:{sex}, 年龄:{age}")

print("1*1=%d" % (1 * 1))
print(f"1*2={1 * 2}")
print("字符串在python的类型:%s" % type("str"))
