# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    urldomain = scrapy.Field()#站点urlmd5编码
    html = scrapy.Field()#html的urlmd5编码
    images = scrapy.Field()
    pdf = scrapy.Field()
    xls = scrapy.Field()
    others = scrapy.Field()