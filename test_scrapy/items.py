# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#item�ļ����ڶ�����ȡ�������ݵ����壬����Ŀ��ĵط�
#�����ȡ�ⷿ��Ϣ����Ŀ�����������壬���ֶα���ͼ۸�
class TestScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()      #field����ָ��ÿ���ֶε�Ԫ����
    money = scrapy.Field()
    #pass