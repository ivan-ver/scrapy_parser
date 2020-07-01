# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import mysql.connector
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ParsPipeline(object):
    def __init__(self):
        self.create_connector()
        self.create_table()

    def create_connector(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='java_dev_blog'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""drop table if exists java_articles""")
        self.curr.execute("""create table java_articles(
                        title text, 
                        author text,
                        p_date text,
                        tags text
                        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        sql_ = 'insert into java_articles (title, author, p_date, tags) values(%s, %s, %s, %s)'
        self.curr.execute(sql_, (item['title'],
                                 item['author'],
                                 item['p_date'],
                                 item['tags']))
        self.conn.commit()


