# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimeItem(scrapy.Item):
    name = scrapy.Field()
    year = scrapy.Field()
    score = scrapy.Field()
    genre = scrapy.Field()
    link = scrapy.Field()
    chat = scrapy.Field()
    image_link = scrapy.Field()
