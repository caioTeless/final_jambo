"""


query = 'Primeira Guerra'

search = GoogleSearch({'q': query,
                       'location': 'Brazil',
                       'hl': 'pt',
                       'gl': 'br',
                       'google_domain': 'google.com',
                       'api_key': 'fdc1f0c741f9e4d410f275b48236f03d38d974bdcb1f3e33308efbdae4661173'})
results = search.get_dict()

for result in results['organic_results']:
    print(result)
"""
# from serpapi import GoogleSearch

results = dict()

results['organic_results'] = {'position': 1, 'title': 'Primeira Guerra Mundial: tudo sobre essa guerra global', 'link': 'https://brasilescola.uol.com.br/historiag/primeira-guerra.htm', 'displayed_link': 'https://brasilescola.uol.com.br › historiag › primeira-gu...', 'snippet': 'A Primeira Guerra Mundial foi um conflito que aconteceu entre 1914 e 1918, e os principais cenários de guerra ocorreram no continente europeu. Foi resultado de ...', 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:IYkaBCcIl7kJ:https://brasilescola.uol.com.br/historiag/primeira-guerra.htm+&cd=1&hl=pt-BR&ct=clnk&gl=br'}, \
{'position': 2, 'title': 'Primeira Guerra Mundial – Wikipédia, a enciclopédia livre', 'link': 'https://pt.wikipedia.org/wiki/Primeira_Guerra_Mundial', 'displayed_link': 'https://pt.wikipedia.org › wiki › Primeira_Guerra_Mun...', 'snippet': 'A Primeira Guerra Mundial (também conhecida como Grande Guerra ou Guerra das Guerras até o início da Segunda Guerra Mundial) foi um conflito bélico global ...', 'sitelinks': {'inline': [{'title': 'Aliados da Primeira Guerra...', 'link': 'https://pt.wikipedia.org/wiki/Aliados_da_Primeira_Guerra_Mundial'}, {'title': 'Causas da Primeira Guerra', 'link': 'https://pt.wikipedia.org/wiki/Causas_da_Primeira_Guerra_Mundial'}, {'title': 'Participantes', 'link': 'https://pt.wikipedia.org/wiki/Participantes_da_Primeira_Guerra_Mundial'}]}, 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:z9XWtf4W7KsJ:https://pt.wikipedia.org/wiki/Primeira_Guerra_Mundial+&cd=2&hl=pt-BR&ct=clnk&gl=br', 'related_pages_link': 'https://www.google.com/search?hl=pt&gl=br&q=related:https://pt.wikipedia.org/wiki/Primeira_Guerra_Mundial+Primeira+Guerra&sa=X&ved=2ahUKEwizme6Nsd7zAhWXl2oFHQYDCn8QH3oECAIQBw'}, \
{'position': 3, 'title': 'Primeira Guerra Mundial: causas e consequências - Mundo ...', 'link': 'https://mundoeducacao.uol.com.br/historiageral/primeira-guerra-mundial.htm', 'displayed_link': 'https://mundoeducacao.uol.com.br › História Geral', 'snippet': 'A Primeira Guerra Mundial foi um conflito envolvendo vários países entre 1914 e 1918, na Europa. As origens remontam a meados do século XIX, ...', 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:yvLap8XG7ycJ:https://mundoeducacao.uol.com.br/historiageral/primeira-guerra-mundial.htm+&cd=16&hl=pt-BR&ct=clnk&gl=br'}, \
{'position': 4, 'title': 'Primeira Guerra Mundial - Toda Matéria', 'link': 'https://www.todamateria.com.br/primeira-guerra-mundial/', 'displayed_link': 'https://www.todamateria.com.br › primeira-guerra-mun...', 'snippet': 'A Primeira Guerra Mundial (1914-1918) foi o resultado dos atritos permanentes provocados pelo imperialismo entre as grandes potências ...', 'rich_snippet': {'top': {'detected_extensions': {'de_out_de': 5}, 'extensions': ['5 de out. de 2020', 'Vídeo enviado por Toda Matéria']}}, 'related_pages_link': 'https://www.google.com/search?hl=pt&gl=br&q=related:https://www.todamateria.com.br/primeira-guerra-mundial/+Primeira+Guerra&sa=X&ved=2ahUKEwizme6Nsd7zAhWXl2oFHQYDCn8QH3oECEIQCA'}, \
{'position': 5, 'title': 'Primeira Guerra Mundial: A Grande Guerra - História do mundo', 'link': 'https://www.historiadomundo.com.br/idade-contemporanea/primeira-guerra-mundial.htm', 'displayed_link': 'https://www.historiadomundo.com.br › primeira-guerra...', 'snippet': 'A Primeira Guerra Mundial, que durou de 1914 a 1918, foi considerada por muitos de seus contemporâneos como a mais terrível das guerras.', 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:rvu6SDI7NbgJ:https://www.historiadomundo.com.br/idade-contemporanea/primeira-guerra-mundial.htm+&cd=21&hl=pt-BR&ct=clnk&gl=br'}, \
{'position': 6, 'title': 'Primeira Guerra Mundial: os conflitos europeus tomam o globo', 'link': 'https://www.politize.com.br/primeira-guerra-mundial-entenda/', 'displayed_link': 'https://www.politize.com.br › primeira-guerra-mundial-...', 'date': '24 de dez. de 2018', 'snippet': 'A Primeira Guerra Mundial (1914-1918) foi um conflito iniciado por países europeus que atingiu uma proporção até então inédita: uma guerra ...', 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:2gQCUbFeFd8J:https://www.politize.com.br/primeira-guerra-mundial-entenda/+&cd=22&hl=pt-BR&ct=clnk&gl=br'}, \
{'position': 7, 'title': 'A história da Primeira Guerra Mundial - Superinteressante', 'link': 'https://super.abril.com.br/especiais/a-historia-da-primeira-guerra-mundial/', 'displayed_link': 'https://super.abril.com.br › especiais › a-historia-da-pri...', 'snippet': 'Considerada o primeiro conflito totalmente mecanizado na história, a guerra travada entre 1914 e 1918 marcou a estréia de diversos equipamentos que até hoje são ...', 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:HgMFnxLBw5IJ:https://super.abril.com.br/especiais/a-historia-da-primeira-guerra-mundial/+&cd=23&hl=pt-BR&ct=clnk&gl=br'}, \
{'position': 8, 'title': 'A Primeira Guerra Mundial - Holocaust Encyclopedia', 'link': 'https://encyclopedia.ushmm.org/content/pt-br/article/world-war-i', 'displayed_link': 'https://encyclopedia.ushmm.org › article › world-war-i', 'snippet': 'A Primeira Guerra Mundial iniciou o primeiro grande conflito internacional do século vinte. O assassinato do arquiduque Francisco Ferdinando, herdeiro do ...', 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:LZZap_q0FFEJ:https://encyclopedia.ushmm.org/content/pt-br/article/world-war-i+&cd=24&hl=pt-BR&ct=clnk&gl=br'}


class CrawlerGeneralContent:

    def __init__(self, query):
        self.query = query
        self.title = []
        self.links = []
        self.preview = []

    # def search_google(self):
        # search = GoogleSearch({'q': self.query,
        #                       'location': 'Brazil',
        #                       'hl': 'pt',
        #                       'gl': 'br',
        #                       'google_domain': 'google.com',
        #                       'api_key': 'fdc1f0c741f9e4d410f275b48236f03d38d974bdcb1f3e33308efbdae4661173'})
        # return search

    def get_results(self):
        # results = self.search_google().get_results()
        for result in results['organic_results']:
            self.links.append(result['link'])
            self.title.append(result['title'])
            self.preview.append(result['snippet'])

    def show_results(self):
        arquive = open('crawler_general.txt', 'w')
        for index, value in enumerate(self.links):
            arquive.writelines(value + '\n')
            arquive.writelines(self.title[index] + '\n')
            arquive.writelines(self.preview[index] + '\n')
            arquive.write('\n')
        arquive.close()


teste_class = CrawlerGeneralContent('Teste')
teste_class.get_results()
teste_class.show_results()

"""
results = {}

results['organic_results'] = {'position': 1, 'title': 'Primeira Guerra Mundial: tudo sobre essa guerra global', 'link': 'https://brasilescola.uol.com.br/historiag/primeira-guerra.htm', 'displayed_link': 'https://brasilescola.uol.com.br › historiag › primeira-gu...', 'snippet': 'A Primeira Guerra Mundial foi um conflito que aconteceu entre 1914 e 1918, e os principais cenários de guerra ocorreram no continente europeu. Foi resultado de ...', 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:IYkaBCcIl7kJ:https://brasilescola.uol.com.br/historiag/primeira-guerra.htm+&cd=1&hl=pt-BR&ct=clnk&gl=br'}, \
{'position': 2, 'title': 'Primeira Guerra Mundial – Wikipédia, a enciclopédia livre', 'link': 'https://pt.wikipedia.org/wiki/Primeira_Guerra_Mundial', 'displayed_link': 'https://pt.wikipedia.org › wiki › Primeira_Guerra_Mun...', 'snippet': 'A Primeira Guerra Mundial (também conhecida como Grande Guerra ou Guerra das Guerras até o início da Segunda Guerra Mundial) foi um conflito bélico global ...', 'sitelinks': {'inline': [{'title': 'Aliados da Primeira Guerra...', 'link': 'https://pt.wikipedia.org/wiki/Aliados_da_Primeira_Guerra_Mundial'}, {'title': 'Causas da Primeira Guerra', 'link': 'https://pt.wikipedia.org/wiki/Causas_da_Primeira_Guerra_Mundial'}, {'title': 'Participantes', 'link': 'https://pt.wikipedia.org/wiki/Participantes_da_Primeira_Guerra_Mundial'}]}, 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:z9XWtf4W7KsJ:https://pt.wikipedia.org/wiki/Primeira_Guerra_Mundial+&cd=2&hl=pt-BR&ct=clnk&gl=br', 'related_pages_link': 'https://www.google.com/search?hl=pt&gl=br&q=related:https://pt.wikipedia.org/wiki/Primeira_Guerra_Mundial+Primeira+Guerra&sa=X&ved=2ahUKEwizme6Nsd7zAhWXl2oFHQYDCn8QH3oECAIQBw'}, \
{'position': 3, 'title': 'Primeira Guerra Mundial: causas e consequências - Mundo ...', 'link': 'https://mundoeducacao.uol.com.br/historiageral/primeira-guerra-mundial.htm', 'displayed_link': 'https://mundoeducacao.uol.com.br › História Geral', 'snippet': 'A Primeira Guerra Mundial foi um conflito envolvendo vários países entre 1914 e 1918, na Europa. As origens remontam a meados do século XIX, ...', 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:yvLap8XG7ycJ:https://mundoeducacao.uol.com.br/historiageral/primeira-guerra-mundial.htm+&cd=16&hl=pt-BR&ct=clnk&gl=br'}, \
{'position': 4, 'title': 'Primeira Guerra Mundial - Toda Matéria', 'link': 'https://www.todamateria.com.br/primeira-guerra-mundial/', 'displayed_link': 'https://www.todamateria.com.br › primeira-guerra-mun...', 'snippet': 'A Primeira Guerra Mundial (1914-1918) foi o resultado dos atritos permanentes provocados pelo imperialismo entre as grandes potências ...', 'rich_snippet': {'top': {'detected_extensions': {'de_out_de': 5}, 'extensions': ['5 de out. de 2020', 'Vídeo enviado por Toda Matéria']}}, 'related_pages_link': 'https://www.google.com/search?hl=pt&gl=br&q=related:https://www.todamateria.com.br/primeira-guerra-mundial/+Primeira+Guerra&sa=X&ved=2ahUKEwizme6Nsd7zAhWXl2oFHQYDCn8QH3oECEIQCA'}, \
{'position': 5, 'title': 'Primeira Guerra Mundial: A Grande Guerra - História do mundo', 'link': 'https://www.historiadomundo.com.br/idade-contemporanea/primeira-guerra-mundial.htm', 'displayed_link': 'https://www.historiadomundo.com.br › primeira-guerra...', 'snippet': 'A Primeira Guerra Mundial, que durou de 1914 a 1918, foi considerada por muitos de seus contemporâneos como a mais terrível das guerras.', 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:rvu6SDI7NbgJ:https://www.historiadomundo.com.br/idade-contemporanea/primeira-guerra-mundial.htm+&cd=21&hl=pt-BR&ct=clnk&gl=br'}, \
{'position': 6, 'title': 'Primeira Guerra Mundial: os conflitos europeus tomam o globo', 'link': 'https://www.politize.com.br/primeira-guerra-mundial-entenda/', 'displayed_link': 'https://www.politize.com.br › primeira-guerra-mundial-...', 'date': '24 de dez. de 2018', 'snippet': 'A Primeira Guerra Mundial (1914-1918) foi um conflito iniciado por países europeus que atingiu uma proporção até então inédita: uma guerra ...', 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:2gQCUbFeFd8J:https://www.politize.com.br/primeira-guerra-mundial-entenda/+&cd=22&hl=pt-BR&ct=clnk&gl=br'}, \
{'position': 7, 'title': 'A história da Primeira Guerra Mundial - Superinteressante', 'link': 'https://super.abril.com.br/especiais/a-historia-da-primeira-guerra-mundial/', 'displayed_link': 'https://super.abril.com.br › especiais › a-historia-da-pri...', 'snippet': 'Considerada o primeiro conflito totalmente mecanizado na história, a guerra travada entre 1914 e 1918 marcou a estréia de diversos equipamentos que até hoje são ...', 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:HgMFnxLBw5IJ:https://super.abril.com.br/especiais/a-historia-da-primeira-guerra-mundial/+&cd=23&hl=pt-BR&ct=clnk&gl=br'}, \
{'position': 8, 'title': 'A Primeira Guerra Mundial - Holocaust Encyclopedia', 'link': 'https://encyclopedia.ushmm.org/content/pt-br/article/world-war-i', 'displayed_link': 'https://encyclopedia.ushmm.org › article › world-war-i', 'snippet': 'A Primeira Guerra Mundial iniciou o primeiro grande conflito internacional do século vinte. O assassinato do arquiduque Francisco Ferdinando, herdeiro do ...', 'cached_page_link': 'https://webcache.googleusercontent.com/search?q=cache:LZZap_q0FFEJ:https://encyclopedia.ushmm.org/content/pt-br/article/world-war-i+&cd=24&hl=pt-BR&ct=clnk&gl=br'}

title = []
links = []
previa = []

for result in results['organic_results']:
    title.append(result['title'])
    links.append(result['link'])
    previa.append(result['snippet'])


for index, value in enumerate(title):
    print('-' * 50)
    print(links[index])
    print(value)
    print(previa[index])

"""
