import scrapy


class JamboCrawler(scrapy.Spider):
    name = 'jogos'
    start_urls = ['https://boardgamegeek.com/browse/boardgame/page/1']

    def parse(self, response):
        for game in response.css('#row_'):
            yield {
                'rank': game.css('.collection_rank a::attr(name)').get(),
                'name': game.css('.primary ::text').get(),
                'average': game.css('#row_ .collection_bggrating:nth-child(5) ::text').get().split()[0]
            }

