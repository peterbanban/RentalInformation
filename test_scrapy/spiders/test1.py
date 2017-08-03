# _*_ coding:utf-8 _*_
#GVIM 添加汉字注释

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import scrapy
from  ..items import TestScrapyItem

class test1Spider(scrapy.Spider):
    name ='test_scrapy'                                 #新建爬虫
    start_urls=['http://bj.ganji.com/fang1/chanyang/']  #定义初始连接

    def parse(self,response):
        test=TestScrapyItem()
        title_list=response.xpath(".//div[@class='f-list-item ']/dl/dd[1]/a/text()").extract()
        money_list=response.xpath(".//div[@class='f-list-item ']/dl/dd[5]/div[1]/span[1]/text()").extract()
        for i in range(0,len(title_list)):
            test['title']=title_list[i]
            test['money']=money_list[i]
            yield test

