#

from urllib import request

url = 'http://www.baidu.com/'

response = request.urlopen(url)

print(type(response))

# content = response.read().decode('utf-8')
# content = response.readline()
# response.readlines()
code = response.getcode()
print(code)
print(response.geturl())
print(response.getheaders())
# print(content)
