from xml.sax.handler import ContentHandler
from xml.sax import parse


class PageMaker(ContentHandler):
    pass_through = False

    def startElement(self, name, attrs):
        if name == 'page':
            self.pass_through = True
            self.out = open(attrs['name'] + '.html', 'w')
            self.out.write('<html><head>\n')
            self.out.write('<title>{}</title>\n'.format(attrs['title']))
            self.out.write('</head><body>\n')
        elif self.pass_through:
            self.out.write('<' + name)
            for key, val in attrs.items():
                self.out.write(' {}="{}"'.format(key, val))
            self.out.write('>')

    def endElement(self, name):
        if name == 'page':
            self.pass_through = False
            self.out.write('\n</body></html>\n')
            self.out.close()
        elif self.pass_through:
            self.out.write('</{}>'.format(name))

    def characters(self, content):
        if self.pass_through:
            self.out.write(content)


parse('website.xml', PageMaker())
