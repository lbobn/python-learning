"""
文件工具模块
"""


def print_file_info(file_name):
    """
    # 打印文件全部内容,若文件不存在则捕获异常,输出错误信息
    :param file_name:
    :return:
    """
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        content = f.read()
        print(content)
    except Exception as e:
        print(f"出现异常{e}")
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    """
    追加写入文件
    :param file_name:
    :param data:
    :return:
    """

    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()


if __name__ == '__main__':
    print_file_info("D:\\Test\\python\\python-learning\\07-文件操作\\test.txt")
    append_to_file("D:\\Test\\python\\python-learning\\07-文件操作\\test.txt", "nihao")
