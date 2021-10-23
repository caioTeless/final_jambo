import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
import pandas as pd

"""
class JamboCrawler(scrapy.Spider):
    name = 'jogos' # Deve ser chamado para rodar o scrapy
    start_urls = ['https://boardgamegeek.com/browse/boardgame/page/1']

    def parse(self, response):
        for game in response.css('#row_'):
            yield {
                'rank': game.css('.collection_rank a::attr(name)').get(),
                'name': game.css('.primary ::text').get(),
                'average': game.css('#row_ .collection_bggrating:nth-child(5) ::text').get().split()[0]
            }

        next_page = response.xpath('//*[@id="maincontent"]/form/div/div[1]/a[5]').attrib['href']

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


# process = CrawlerProcess('HEADER')
# process.crawl(JamboCrawler)
# process.start()
"""


class JamboCrawler(scrapy.Spider):
    name = 'jambo'

    # allowed_domains = ['tecnoblog.net']
    start_urls = ['https://www.google.com/search?q=historia&sxsrf=AOaemvLFoV6x1w80UFmprVmjaAsWBY-iTw%3A1634841187670&ei=Y7JxYY-vKObWytMPlMuMqAU&ved=0ahUKEwjP7ISCktzzAhVmq3IEHZQlA1UQ4dUDCA4&uact=5&oq=historia&gs_lcp=Cgdnd3Mtd2l6EAMyDgguEMcBENEDEMsBEJMCMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCC4QywEyBQgAEMsBOgcIIxCwAxAnOgcIABBHELADOgQIIxAnOgYIIxAnEBM6BAgAEEM6CwguEIAEEMcBEKMCOgUIABCABDoLCC4QgAQQxwEQrwE6CgguEMcBENEDEEM6CwguEIAEEMcBENEDSgQIQRgAULMbWMEgYPwhaANwAngAgAGqAogB0AuSAQMyLTaYAQCgAQHIAQnAAQE&sclient=gws-wiz']

    def parse(self, response):
        xlink = LinkExtractor()
        for link in xlink.extract_links(response):
            if len(str(link)) > 200 or 'Journal' in link.text:
                print(len(str(link)), link.text, link, '\n')



