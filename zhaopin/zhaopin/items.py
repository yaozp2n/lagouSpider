# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhaopinItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    company = scrapy.Field()
    date = scrapy.Field()
    salary = scrapy.Field()
    work_year = scrapy.Field()
    education = scrapy.Field()
    position = scrapy.Field()
    address = scrapy.Field()

