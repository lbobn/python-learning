import urllib.request
from lxml import etree
import re


# https://sc.chinaz.com/tupian/keaitupian.html  第一页
# https://sc.chinaz.com/tupian/keaitupian_2.html 第二页
# https://sc.chinaz.com/tupian/201223428714.htm 图片点击后

# https://scpic3.chinaz.net/Files/pic/pic9/202012/apic29623_s.jpg  缩略
# https://scpic.chinaz.net/files/pic/pic9/202012/apic29623.jpg   高清


def create_request(page):
    if page == 1:
        url = "https://sc.chinaz.com/tupian/keaitupian.html"
    else:
        url = "https://sc.chinaz.com/tupian/keaitupian_" + str(page) + ".html"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/116.0.1938.69'
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request


def getContent(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def download(content):
    # 解析
    tree = etree.HTML(content)
    url_list: list[str] = tree.xpath('//div[@class="container"]//img/@data-original')
    name_list = tree.xpath('//div[@class="container"]//img/@alt')
    for i in range(len(url_list)):
        # 替换为高清图片的url
        # 正则替换
        regex1 = re.compile("scpic(\d)+")
        new_url = regex1.sub('scpic', url_list[i])
        # replace
        new_url = new_url.replace("Files", "files")
        new_url = new_url.replace("_s", "")
        # 拼接最终url
        img_url = 'https:' + new_url
        # 下载
        urllib.request.urlretrieve(img_url, './zhanzhang/' + str(name_list[i] + ".jpg"))


if __name__ == '__main__':
    start_page = int(input("请输入起始页"))
    end_page = int(input("请输入结束页"))
    for page in range(start_page, end_page + 1):
        # print(page)
        # 请求对象定制
        request = create_request(page)
        # 获取网页源码
        content = getContent(request)
        # 下载
        download(content)
