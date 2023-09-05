import urllib.request
import urllib.parse

# url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
url = 'https://fanyi.baidu.com/langdetect'
# url = 'https://fanyi.baidu.com/transapi'

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/116.0.1938.69'
}

# data = {
#     'query': 'hello'
# }

data = {
    "from": "en",
    "to": "zh",
    "source": "txt",
    "query": "hello"
}
data = urllib.parse.urlencode(data).encode('utf-8')

# print(data)
request = urllib.request.Request(url, data, headers)

response = urllib.request.urlopen(request)

result = response.read().decode('utf-8')

# print(result)

import json

new_result = json.loads(result)

print(new_result)
