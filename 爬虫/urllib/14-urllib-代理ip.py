import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

proxies = {
    # 代理ip
    'http': '222.74.73.202:42055'
}

headers = {
    'User-Agent': 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
}

request = urllib.request.Request(url, headers=headers)

handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')
with open("daili.html", "w", encoding='utf-8') as fp:
    fp.write(content)
