# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

#from itemadapter import ItemAdapter


# class MyspiderPipeline:
#     def process_item(self, item, spider):
#         return item

import pymongo
from itemadapter import ItemAdapter

#使用mongodb存储资源对应关系

class MongoPipeline:
    collection_name = 'scrapy_gov_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        '''
            scrapy为我们访问settings提供了这样


            的一个方法，这里，
            我们需要从settings.py文件中，取得数据库的URI和数据库名称
        '''

        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        '''
            爬虫一旦开启，就会实现这个方法，连接到数据库
        '''
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        '''
        爬虫一旦关闭，就会实现这个方法，关闭数据库连接
        '''
        self.client.close()


#插入数据
    def process_item(self, item, spider):
        '''
            每个实现保存的类里面必须都要有这个方法，且名字固定，用来具体实现怎么保存
        '''

        table = self.db[self.collection_name]
        table.insert_one(ItemAdapter(item).asdict())
        return item

