import urllib.request
import urllib.error

# 模拟参数错误
url = 'https://blog.csdn.net/qwe546912/article/details/132639931'
# 模拟网址错误
new_url = 'https://www.csdnjkvs.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/116.0.1938.69'
}
try:
    request = urllib.request.Request(new_url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError:
    print("系统正在升级")
except urllib.error.URLError:
    # 网址错误
    print("系统还在升级")
