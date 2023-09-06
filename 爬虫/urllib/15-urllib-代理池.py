import urllib.request
import random

url = 'http://www.baidu.com/s?wd=ip'

proxies_pool = [
    {'http': '117.26.40.99:888811'},
    {'http': '117.26.40.99:888822'},
    {'http': '117.26.40.99:888833'},
]

proxies = random.choice(proxies_pool)
print(proxies)

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/116.0.1938.69'
# }
#
# request = urllib.request.Request(url, headers=headers)
#
# handler = urllib.request.ProxyHandler(proxies=proxies)
#
# opener = urllib.request.build_opener(handler)
#
# response = opener.open(request)
#
# content = response.read().decode('utf-8')
# with open("daili.html", "w", encoding='utf-8') as fp:
#     fp.write(content)

# print(content)
