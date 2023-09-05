# 1
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 上海
# pid:
# pageIndex: 1
# pageSize: 10

# 2
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 上海
# pid:
# pageIndex: 2
# pageSize: 10

import urllib.request
import urllib.parse


def get_request(page):
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/116.0.1938.69'
    }
    data = {
        "cname": "上海",
        "pid": "",
        "pageIndex": page,
        "pageSize": 10
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url, data, headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def download(page, content):
    with open(f"kfc_download/kfc_{page}.json", 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input("请输入起始页"))
    end_page = int(input("请输入结束页"))
    for page in range(start_page, end_page + 1):
        # print(page)
        # 请求对象定制
        request = get_request(page)
        # 获取响应结果
        content = get_content(request)
        # 下载
        download(page, content)
