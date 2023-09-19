url = 'https://www.baidu.com/s?wd=周杰伦'

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/116.0.1938.69'
}

data = {
    "wd": '周杰伦'
}

response = requests.get(url=url, params=data, headers=headers)

print(response.text)
