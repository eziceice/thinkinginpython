def helloworld(greeting, name):
    print(greeting + ', ' + name)

helloworld(greeting='hello', name='world')


def helloworld_1(greeting='Hello',name='world'):
    print(greeting + ', ' + name)

helloworld_1()

def print_params(*params, **keypar):
    print(params, keypar)

print_params('1')

print_params('1','2',3)

print_params('1','2', key1=['1234'], key2=2)