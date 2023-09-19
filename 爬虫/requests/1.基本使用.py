import requests
url = "http://www.baidu.com"
response = requests.get(url)

# response.text
# response.encoding
# response.url
# response.content
# response.status_code
# response.headers

print(response.text)
