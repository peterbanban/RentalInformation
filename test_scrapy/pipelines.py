# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
class TestScrapyPipeline(object):
    def open_spider(self,spider):   #������ʱ�ܵ����ӵ����ݿ�
        self.con=sqlite3.connect('test_scrapy.sqlite')    #�������ݿ�
        self.cu=self.con.cursor()                         #����ִ�������
  
    def process_item(self, item, spider):    #���湤��ʱ����ȡ�������ݴ������ݿ�
        print(spider.name,'pipelines')
        insert_sql="insert into test_scrapy (title, money) values('{}','{}')".format(item['title'],item['money'])
        print (insert_sql.decode('utf-8'))
        self.cu.execute(insert_sql)          #�������
        self.con.commit()                    #�ύ�����ݿ�
        return item

    def close_spider():             #����ر�ʱ�����ݿ�����Ҳ�رյ�
        self.con.close()