# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CrawlspiderPipeline:
    def open_spider(self, spider):
        self.fp = open('book.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    def close_spider(self, spider):
        self.fp.close()


from scrapy.utils.project import get_project_settings
import pymysql


class MySQLCrawlspiderPipeline:
    def open_spider(self, spider):
        settings = get_project_settings()
        self.DB_HOST = settings['DB_HOST']
        self.DB_PORT = settings['DB_PORT']
        self.DB_USER = settings['DB_USER']
        self.DB_PASSWORD = settings['DB_PASSWORD']
        self.DB_NAME = settings['DB_NAME']
        self.DB_CHARSET = settings['DB_CHARSET']

        self.__connect()

    def process_item(self, item, spider):
        sql = 'insert into book(name,src) values ("{}","{}")'.format(item['name'], item['src'])
        self.cursor.execute(sql)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

    def __connect(self):
        self.conn = pymysql.Connection(host=self.DB_HOST,
                                       port=self.DB_PORT,
                                       user=self.DB_USER,
                                       password=self.DB_PASSWORD,
                                       db=self.DB_NAME,
                                       charset=self.DB_CHARSET)
        self.cursor = self.conn.cursor()
