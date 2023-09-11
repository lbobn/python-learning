from bs4 import BeautifulSoup
import urllib.request

url = "https://www.starbucks.com.cn/menu/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/116.0.1938.69'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# xpath = //ul[@class="grid padded-3 product"]//strong
soup = BeautifulSoup(content, 'lxml')
name_list = soup.select('ul[class="grid padded-3 product"] strong')
# print(name_list)
for name in name_list:
    print(name.string)  # 或者name.getText()
