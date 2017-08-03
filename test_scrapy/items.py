# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#item文件用于定义爬取到的数据的载体，是项目类的地方
#针对爬取租房信息的项目定义了类载体，有字段标题和价格
class TestScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()      #field用于指明每个字段的元数据
    money = scrapy.Field()
    #pass
