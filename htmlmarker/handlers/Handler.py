class Handler:

    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None) #第二个参数为方法名, 第三个参数是默认值如果获取不到
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
        return substitution()


from handlers import HTMLRenderer
handler = HTMLRenderer()
handler.sub('emphasis')
import re
re.sub(r'\*(.+?)\*', handler.sub('emphasis'), 'This *is* a test')