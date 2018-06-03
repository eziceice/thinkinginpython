def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        '''
           判断新增加的皇后和之前的是否冲突:
           冲突条件1: 在同一行 state[i] = state[nextX]
           冲突条件2: 在同一对角线 abs(state[i] - state[nextX]) = nextX - i
        '''
        if state[i] == state[nextX] or abs(state[i] - state[nextX]) == nextX - i:
            return True
    return False


def queens(num, state):
    if len(state) == num - 1:
        for pos in range(num):
            if not conflict(state, pos):
                yield pos


def queensrecurision(num=8,state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queensrecurision(num, state + (pos,)):
                    yield (pos,) + result

def prettyprint(soulution):
    def line(pos, length=len(soulution)):
        return '.' * pos + 'X' + '.' * (length - pos - 1)
    for pos in soulution:
        print(line(pos))

