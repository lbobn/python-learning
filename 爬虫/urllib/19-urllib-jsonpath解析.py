import json
import jsonpath

json = json.load(open('书.json', 'r', encoding='utf-8'))

# print(json)

# 所有book的author节点
title_list = jsonpath.jsonpath(json, '$.store.book[*].author')
# print(title_list)

# 所有author节点
author_list = jsonpath.jsonpath(json, '$..author')
# print(author_list)

# store下的所有节点
store_list = jsonpath.jsonpath(json,'$.store.*')
# print(store_list)

# store下的所有price节点
price_list = jsonpath.jsonpath(json, '$.store..price')
# print(price_list)

# 第三个book节点
book_3 = jsonpath.jsonpath(json, '$..book[2]')
# print(book_3)

# 倒数第一个book节点
book_last = jsonpath.jsonpath(json, '$..book[(@.length-1)]')
# $..book[-1:]
# print(book_last)

# 前两个book节点
book_pre2 = jsonpath.jsonpath(json, '$..book[:2]')
# $..book[0,1]
# print(book_pre2)

# 过滤含ISBN的节点
isbn_list = jsonpath.jsonpath(json, '$..book[?(@.isbn)]')
# print(isbn_list)

# 过滤price<10的节点
price_list10 = jsonpath.jsonpath(json, '$..book[?(@.price<10)]')
# print(price_list10)

# 递归匹配所有子节点
all_list = jsonpath.jsonpath(json, '$..*')
# print(all_list)