# 用于定制更高级的请求对象
import urllib.request

url = "https://www.baidu.com/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/116.0.1938.69'
}

request = urllib.request.Request(url, headers=headers)

# 获取handler对象
handler = urllib.request.HTTPHandler()
# 传入handler对象
opener = urllib.request.build_opener(handler)
# 调用open()
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)
