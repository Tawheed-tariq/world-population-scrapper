# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class WorldPopulationPipeline:
    
    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = sqlite3.connect('world-population.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.conn.execute(""" DROP TABLE IF EXISTS population_by_country """)
        self.conn.execute(
            """
            create table population_by_country(
                country,
                population,
                land area,
                world share
            )
            """
        )
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self, item):
        self.conn.execute("""
            insert into population_by_country values(?, ? ,? ,?)""", (
                item['country'][0],
                item['population'][0],
                item['land_area'][0],
                item['world_share'][0],
            ))
        self.conn.commit()