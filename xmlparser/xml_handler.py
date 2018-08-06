from xml.sax.handler import ContentHandler
from xml.sax import parse
from xmlparser import website


class HeadlineHandler(ContentHandler):
    in_headline = False

    def __init__(self, headlines):
        super().__init__()
        self.headlines = headlines
        self.data = []

    def startElement(self, name, attrs):
        if name == 'h1':
            self.in_headline = True

    def endElement(self, name):
        if name == 'h1':
            text = ''.join(self.data)
            self.data = []
            self.headlines.append(text)
            self.in_headline = False

    def characters(self, content):
        if self.in_headline:
            self.data.append(content)


class TestHandler(website.Dispatcher, ContentHandler):

    def start_page(self, attrs):
        print('Beginning page', attrs['name'])

    def end_page(self):
        print('Ending Page')