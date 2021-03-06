# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
class TestScrapyPipeline(object):
    def open_spider(self,spider):   #打开爬虫时管道连接到数据库
        self.con=sqlite3.connect('test_scrapy.sqlite')    #连接数据库
        self.cu=self.con.cursor()                         #插入执行命令定义
  
    def process_item(self, item, spider):    #爬虫工作时将爬取到的数据存入数据库
        print(spider.name,'pipelines')
        insert_sql="insert into test_scrapy (title, money) values('{}','{}')".format(item['title'],item['money'])
        print (insert_sql.decode('utf-8'))
        self.cu.execute(insert_sql)          #插入语句
        self.con.commit()                    #提交到数据库
        return item

    def close_spider():             #爬虫关闭时将数据库连接也关闭掉
        self.con.close()
