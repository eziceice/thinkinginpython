class Dispatcher:

    def startElement(self, name, attrs):
        self.dispatch('start', name, attrs)

    def endElement(self, name):
        self.dispatch('end', name)

    def dispatch(self, prefix, name, attrs=None):
        """
        1. 根据前缀('start'或者'end')和标签名(如'page'),生成处理程序的名称('startPage')
        2. 根据前缀生成默认处理程序的名称('defaultStart')
        3. 尝试使用getattr获取处理程序, 并将默认值设置为None
        4. 如果结果是可以调用的, 就将args设为一个空tuple
        5. 否则, 就尝试使用getattr获取默认处理程序, 并将默认值也设为None, 另外将args设置为一个只包含标签名的元组 - 默认处理程序只需要标签名
        6. 如果要调用的是起始处理程序, 就将属性添加到参数tuple中.
        7. 如果获得的处理程序时可调用的(默认或存在的), 就使用正确的参数调用它.
        :param prefix:
        :param name:
        :param attrs:
        :return:
        """
        mname = prefix + name.capitalize()
        dname = 'default ' + prefix.capitalize()
        method = getattr(self, mname, None)
        if callable(method):
            args = ()
        else:
            method = getattr(self, dname, None)
            args = name,  # 设为tuple时后面要加,
        if prefix == 'start':
            args += attrs,
        if callable(method):
            method(*args)

    def writeHeader(self, title):
        self.out.write("<html>\n <head>\n <title>")
        self.out.write(title)
        self.out.write("</title>\n </head>\n <body>\n")

    def writeFooter(self):
        self.out.write("\n </body>\n</html>\n")
