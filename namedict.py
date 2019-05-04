def testDict():
    people = {
        'Alice': {
            'phone': '2341',
            'addr': 'Foo drive 23'
        },
        'Beth': {
            'phone': '9102',
            'addr': 'Bar street 42'
        },
        'Cecil': {
            'phone': '3158',
            'addr': 'Baz avenue 90'
        }
    }

    labels = {
        'phone': 'phone number',
        'addr': 'address'
    }

    name = raw_input('Name: ')

    request = raw_input('Phone number (p) or address (a)? ')

    if request == 'p':
        key = 'phone'
    if request == 'a':
        key = 'addr'

    if name in people:
        print(name + ' ' + labels[key] + ' ' + people[name][key])

def testdict2():
    storage = {}
    storage['first'] = {}
    storage['middle'] = {}
    storage['last'] = {}
    me = 'Magnus Lie Hetland'
    storage['first']['Magnus'] = [me]
    storage['middle']['Lie'] = [me]
    storage['last']['Hetland'] = [me]

    my_sister = 'Anne Lie HetLand'
    storage['first'].setdefault('Anne',[]).append(my_sister)
    storage['middle'].setdefault('Lie',[]).append(my_sister)
    print(storage['first'])
    print(storage['middle'])


testdict2()