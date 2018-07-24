class Rule:
    """
    对于每种文本块, 都制定一条相应的规则. 这些规则能够检测不同类型的文本块并相应地设置格式
    """

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True


class HeadlineRule(Rule):
    """
    标题只包含一行, 不超过70个字符并且不用冒号结尾
    """
    type = 'heading'

    def condition(self, block):
        """
        如果文本块符合标题的定义, 就返回True
        :param block:
        :return:
        """
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'

    def action(self, block, handler):
        """
        调用诸如handler.start, hanlder.feed, handler.end等方法
        不想尝试其他规则, 则返回True, 以结束对当前文本块的处理
        :param block:
        :param handler:
        :return:
        """
        pass


class TitleRule(Rule):
    """
    题目是文档中的第一个文本块, 前提条件是它是个标题
    """
    type = 'title'
    first = True

    def condition(self, block):
        if not self.first:
            return False
        return HeadlineRule.condition(self, block)


class ListItemRule(Rule):
    """
    列表项是以连字符打头的段落. 在设置格式的过程中, 将把连字符删除
    """
    type = 'listitem'

    def condition(self, block):
        return block[0] == '-'

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True


class ListRule(ListItemRule):
    """
    列表以紧跟在非列表项文本块后面的列表项开头,
    以相连的最后一个列表项结束
    """
    type = 'list'
    inside = False

    def condition(self, block):
        return True

    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False


class ParagraphRule(Rule):
    """
    段落是不符合其他规则的文本块
    """
    type = 'paragraph'

    def condition(self, block):
        return True