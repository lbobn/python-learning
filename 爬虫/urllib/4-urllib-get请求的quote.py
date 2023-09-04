import urllib.request
import urllib.parse

url = 'https://www.baidu.com/s?wd='

name = urllib.parse.quote('周杰伦')

url = url + name
# print(url)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode('utf8'))
