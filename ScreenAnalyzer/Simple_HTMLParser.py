from urllib import request
from html.parser import HTMLParser

class Scraper(HTMLParser):
    in_h3 = False
    in_link = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h3':
            self.in_h3 = True

        if tag == 'a' and 'herf' in attrs:
            self.in_link = True
            self.chunks = []
            self.url = attrs['href']

    def handle_data(self, data):
        if self.in_link:
            self.chunks.append(data)

    def handle_endtag(self, tag):
        if tag == 'h3':
            self.in_h3 = False
        if tag == 'a':
            if self.in_h3 and self.in_link:
                print(self.chunks, self.url)
                self.in_link = False

text = request.urlopen('https://www.google.com').read()
text = bytes.decode(text)
parser = Scraper()
parser.feed(text) #解析HTML
parser.close()