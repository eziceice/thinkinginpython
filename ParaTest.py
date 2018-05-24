def story(**kwds):
    return 'Once upon a time, there was a %(job)s called %(name)s.' %kwds

def power(x, y, *others):
    if others:
        print('Received redundant parameters :', others)
    return pow(x, y)

def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None:
        start, stop = 0, start #此处交换两个值
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result

print(story(job='king',name='Gumby'))
params = (5,)*2
print(power(*params))

print(interval(10))