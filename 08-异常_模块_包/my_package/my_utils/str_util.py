"""
字符串工具模块
"""


def str_reverse(s):
    """
    反转字符串
    :param s:
    :return:
    """
    return s[::-1]


def substr(s, x, y):
    """
    字符串切片
    :param s:
    :param x:
    :param y:
    :return:
    """
    return s[x:y]


if __name__ == '__main__':
    print(str_reverse("你好"))
    print(substr("helloworld", 6, 9))
