# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyDangdang02Pipeline:
    def open_spider(self, spider):
        self.fp = open('book.json', 'w', encoding='utf-8')

    # 设置管道并在settings开启管道
    # item 即为  book 对象
    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    def close_spider(self, spider):
        self.fp.close()


import urllib.request


# 开启多管道
#  1.定义管道类
#  2.在settings中开启管道
class ScrapyDangdangDownload:
    def process_item(self, item, spider):
        url = 'http:' + item.get('src')
        name = './book/' + item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=url, filename=name)
        return item