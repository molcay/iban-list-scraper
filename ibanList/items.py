# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IBANItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    detail_url = scrapy.Field()
    data = scrapy.Field()
    flag_url = scrapy.Field()
    flag = scrapy.Field()


