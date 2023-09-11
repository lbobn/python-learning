import urllib.request
from lxml import etree

url = 'https://www.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/116.0.1938.69'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# print(content)
# with open("baidu.html","w",encoding='utf-8') as fp:
#     fp.write(content)
tree = etree.HTML(content)

result = tree.xpath('//button[@id="index-bn"]/text()')

print(result)
