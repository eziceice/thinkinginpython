def findMinAndMax(L):
    min = None
    max = None
    for i in L:
        if max is None and min is None:
            max = i
            min = i
        elif i > max:
            max = i
        elif i < min:
            min = i
    return min, max

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')