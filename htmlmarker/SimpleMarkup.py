import sys, re

from rules.Rule import *
from Util import *
from handlers.Handler import *

"""
运行时从console cd到对应的路径然后运行
python SimpleMarkup.py < test_input.txt > test_output.html
即可生成对应的html文件
"""


class Parser:
    """
    读取文本文件, 应用规则并控制处理程序的解析器
    """

    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):  # 创建一个过滤器
            return re.sub(pattern, handler.sub(name), block)  # sub pattern为正则, 第二个参数为要替换的字符串(可为函数), 第三个参数为原始字符串

        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)

            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last:
                        break
        self.handler.end('document')


class BasicTextParser(Parser):
    """
    在构造函数中添加规则和过滤器的Parser子类
    """
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadlineRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?\*)', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')


handler = HTMLRenderer()
parser = BasicTextParser(handler)

parser.parse(sys.stdin)