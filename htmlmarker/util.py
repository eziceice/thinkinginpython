def lines(file):
    """
    遍历整个文件并且在文件最后加一个空行
    :param file:
    :return:
    """
    for line in file:
        yield line  # yield和return基本相同, 但是yield会记录之前程序的位置,
        # 调用next或者send方法可以继续使用yield之前的值, 同时生成器也可以在迭代器中使用.
    yield '\n'


def blocks(file):
    """
    生成一个块之后, 就获得一个块的字符串
    :param file:
    :return:
    """
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
