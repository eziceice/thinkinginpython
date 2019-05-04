def simple_generator(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new

s = simple_generator(15)
print(s.__next__())
print(s.__next__())
print(s.send(20))