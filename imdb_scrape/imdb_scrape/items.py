# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbScrapeItem(scrapy.Item):
    rating_score = scrapy.Field()
    rating_count = scrapy.Field()
    genre = scrapy.Field()
    budget = scrapy.Field()
    gross_usa = scrapy.Field()
