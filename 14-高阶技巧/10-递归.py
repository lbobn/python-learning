"""
递归操作
    找出文件夹中所有文件
"""

import os


def test_os():
    print(os.listdir("D:\\Test\\python\\python-learning\\my_package"))  # 列出路径下的内容
    print(os.path.isdir("D:\\Test\\python\\python-learning\\my_package"))  # 判断指定路径是不是文件夹
    print(os.path.exists("D:\\Test\\python\\python-learning\\my_package"))  # 判断指定路径是否存在


def get_file_recursion_from_dir(path):
    """
    从指定路径或去所有文件列表
    :param path:
    :return:
    """
    file_list = []

    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + "\\" + f
            if os.path.isdir(new_path):
                # 是文件夹
                file_list += get_file_recursion_from_dir(new_path)
            else:
                # 是文件
                file_list.append(new_path)

    else:
        print(f"路径{path}不存在")
        return []
    return file_list


if __name__ == '__main__':
    # test_os()
    print(get_file_recursion_from_dir("D:\\Test\\python\\python-learning\\my_package"))
