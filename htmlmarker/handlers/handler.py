class Handler:
    """
    处理程序 - 供解析器用来生成输出, 每个处理程序都生成不同的标记
    """

    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)  # 第二个参数为方法名, 第三个参数是默认值如果获取不到
        if callable(method):
            return method(*args)

    def start(self, name):
        self.callback('start_', name)

    def end(self, name):
        self.callback('end_', name)

    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None:
                match.group(0)
            return result

        return substitution


class HTMLRenderer(Handler):
    """
    用于渲染HTML的具体处理程序

    HTMLRenderer的方法可以通过超类Handler的方法start(),
    end()和sub()来访问. 这些方法实现了HTML文档使用的基本标记
    """

    def start_document(self):
        print('<html><head><title>...</title></head><body>')

    def end_document(self):
        print('</body></html>')

    def start_paragraph(self):
        print('<p>')

    def end_paragraph(self):
        print('</p>')

    def start_heading(self):
        print('<h2>')

    def end_heading(self):
        print('</h2>')

    def start_listitem(self):
        print('<li>')

    def end_listitem(self):
        print('</li>')

    def start_title(self):
        print('<h1>')

    def end_title(self):
        print('</h1>')

    def sub_emphasis(self, match):
        return '<em>{}</em>'.format(match.group(1))

    def sub_url(self, match):
        return '<a href = "{}">{}</a>'.format(match.group(1), match.group(1))

    def sub_mail(self, match):
        return '<a href = "mailto:{}">{}</a>'.format(match.group(1), match.group(1))

    def feed(self, data):
        print(data)

