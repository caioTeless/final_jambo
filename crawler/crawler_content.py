import requests
from bs4 import BeautifulSoup


class CrawlerContent:

    def __init__(self, query, cont):
        self.query = query
        self.cont = cont

    def get_page(self):
        html = requests.get('https://pt.wikipedia.org/wiki/Primeira_Guerra_Mundial', headers='')
        bs = BeautifulSoup(html.text, 'html.parser')
        print(bs.find('h1'))
        # lines = bs.find_all(('p', {'class': 'mw-content-text'}))
        # body = ''.join([line.text for line in lines])
        # for n in ''.join(lines):
        #     print(n)


teste = CrawlerContent('', '')

teste.get_page()
