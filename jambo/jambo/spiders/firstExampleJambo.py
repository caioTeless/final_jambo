"""import scrapy


class FirstexamplejamboSpider(scrapy.Spider):
    name = 'firstExampleJambo'
    start_urls = ['https://boardgamegeek.com/browse/boardgame/page/1']

    def parse(self, response): # Le a página e traz informação.
        response.css('#row_').get()
        response.css('.collection_rank a::attr(name)').get()
        response.css('.primary ::text').get()

        pass
"""
import random

win = random.randint(1, 3000)

print(win)