list_1 = [1, 2, 3, 4, 5]


def list_while_func(new_list):
    """
    while循环遍历list
    :param new_list:
    :return:
    """
    i = 0
    while i < len(new_list):
        print(new_list[i])
        i += 1


def list_for_func(new_list):
    """
    for循环遍历list
    :param new_list:
    :return:
    """
    for element in new_list:
        print(element)


list_while_func(list_1)

list_for_func(list_1)
