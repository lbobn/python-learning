"""
列表的sort排序方法
"""

l = [["a", 33], ["b", 24], ["c", 54]]


def choose_sort_key(element):
    """
    排序依据
    :param element:
    :return:
    """
    return element[1]


# l.sort(key=choose_sort_key, reverse=True)


l.sort(key=lambda element: element[1], reverse=True)
print(l)
