import requests

url = 'https://ip.900cha.com/'

proxies = {
    # 代理ip
    'http': '222.74.73.202:42055'
}

headers = {
    'User-Agent': 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
}

response = requests.get(url=url, headers=headers, proxies=proxies)

print(response.text)
