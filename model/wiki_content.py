class WikiContent:

    def __init__(self, url='', content=''):
        self.url = url
        self.content = content

    def return_content(self):
        return self.content

    def return_urls(self):
        return self.url