# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Article(Item):
    title = Field()
    author = Field()
    p_date = Field()
    tags = Field()
