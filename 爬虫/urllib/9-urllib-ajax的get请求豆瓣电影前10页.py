# https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&
# start=0&limit=20
# https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&
# start=20&limit=20
# https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&
# start=40&limit=20

import urllib.parse
import urllib.request


def get_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/116.0.1938.69'
    }

    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }

    data = urllib.parse.urlencode(data)
    # print(data)
    return urllib.request.Request(f"{base_url}{data}", headers=headers)


def get_response(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def download(page, content):
    with open(f"douban_download/douban_{page}.json", "w", encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start = int(input("请输入起始页码"))
    end = int(input("请输入结束页码"))

    for page in range(start, end + 1):
        # print(page)
        # 请求对象定制
        request = get_request(page)
        # 获取响应结果
        content = get_response(request)
        # 下载本地
        download(page, content)
