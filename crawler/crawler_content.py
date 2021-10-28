import requests
from bs4 import BeautifulSoup
from googlesearch import search
import re

from model.wiki_content import WikiContent


class CrawlerContent:

    site_caught = set()
    wiki_content = list()

    def __init__(self, query='', cont=0):
        self.query = query
        self.cont = cont

    def get_page(self):
        sites = set()
        with open('../main/data.txt', 'w+', encoding='utf-8') as my_data:
            try:
                for searchs in search(self.query, lang='pt-BR', num=self.cont, stop=self.cont, pause=5):
                    sites.add(searchs)
                for site in sites:
                    html = requests.get(site, headers='')
                    bs = BeautifulSoup(html.text, 'html.parser')
                    if 'https://pt.wikipedia.org/wiki/' in site:
                        self.site_caught.add(site)
                        lines = bs.find_all(('p', {'class': 'mw-content-text'}))
                        body = ''.join([line.text for line in lines])
                        wiki = WikiContent(content=body)
                        format_data = re.sub('\[(.*?)\]', '', wiki.return_content())
                        my_data.writelines(format_data) # Corrigir

            except Exception:
                return False


teste = CrawlerContent('Primeira guerra mundial', 5)

teste.get_page()
