import Handler

class HTMLRenderer(Handler):

    def start_paragraph(self):
        print('<p>')

    def end_paragraph(self):
        print('</p>')

    def sub_emphasis(self, match):
        return '<em>{}</em>'.format(match.group(1))

    def feed(self, data):
        print(data)
