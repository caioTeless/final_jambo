import requests
from bs4 import BeautifulSoup
from googlesearch import search
import re

from model.wiki_content import WikiContent
from model import jambo_header


class CrawlerContent:
    wiki_content = set()

    def __init__(self, query=''):
        self.query = query
        self.cont = 10
        self.title = ''

    def get_page(self):
        sites = set()
        with open('../main/data.txt', 'w+', encoding='utf-8') as my_data:
            try:
                for searchs in search(self.query, lang='pt-BR', num=self.cont, stop=self.cont, pause=5):
                    sites.add(searchs)
                for site in sites:
                    html = requests.get(site, headers=jambo_header.headers)
                    bs = BeautifulSoup(html.text, 'html.parser')
                    if 'https://pt.wikipedia.org/wiki/' in site:
                        self.wiki_content.add(site)
                        lines = bs.find_all(('p', {'class': 'mw-content-container'}))
                        body = ''.join([line.text for line in lines])
                        wiki = WikiContent(content=body)
                        format_data = re.sub("\[(.*?)\]", '', wiki.return_content())
                        new = format_data.replace('\t', '')
                        my_data.write(site + '\n\n')
                        my_data.write(new.replace('\n', ''))
            except Exception:
                return

