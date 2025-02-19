# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QuotesTutoPipeline:

    def _init_(self):
        self.create_connection()
        self.create_table()
        

    def create_connection(self):
        self.conn = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password ='tops?123',
            database = 'ws'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""
            CREATE TABLE IF NOT EXISTS q_tb (
                id INT AUTO_INCREMENT PRIMARY KEY,
                quotes TEXT,
                author VARCHAR(255),
                tags TEXT
            )
        """)
        self.conn.commit()
        

    def process_item(self, item, spider):
        self.curr.execute("""
            INSERT INTO q_tb (quotes, author, tags) 
            VALUES (%s, %s, %s)
        """, (
            item['quotes'][0] if item['quotes'] else '', 
            item['author'][0] if item['author'] else '', 
            ', '.join(item['tags']) if item['tags'] else ''
        ))
        self.conn.commit()
        return item
    
    def close_spider(self, spider):
        self.conn.close