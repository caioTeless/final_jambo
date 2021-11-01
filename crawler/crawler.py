from serpapi import GoogleSearch


class CrawlerGeneralContent:

    def __init__(self, query=''):
        self.query = query
        self.title = []
        self.links = []
        self.preview = []

    def search_google(self):
        search = GoogleSearch({'q': self.query,
                               'location': 'Brazil',
                               'hl': 'pt',
                               'gl': 'br',
                               'google_domain': 'google.com',
                               'api_key': 'fdc1f0c741f9e4d410f275b48236f03d38d974bdcb1f3e33308efbdae4661173'})
        return search

    def get_results(self):
        results = self.search_google().get_dict()
        for result in results['organic_results']:
            self.links.append(result['link'])
            self.title.append(result['title'])
            self.preview.append(result['snippet'])
        arquive = open('crawler_general.txt', 'w', encoding='utf-8')
        for index, value in enumerate(self.links):
            arquive.writelines(value + '\n')
            arquive.writelines(self.title[index] + '\n')
            arquive.writelines(self.preview[index] + '\n')
            arquive.write('\n')
        arquive.close()


