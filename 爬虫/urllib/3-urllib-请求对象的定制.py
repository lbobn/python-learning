import urllib.request
import urllib.parse

url = 'https://www.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

# 定制请求对象，其中headers参数需要关键字传参
request = urllib.request.Request(url, headers=headers)

# 传入请求对象，打开url
response = urllib.request.urlopen(request)

print(response.read().decode('utf8'))
