import sys,shelve

def store_person(db):
    pid = input('Enter unique 10 number: ')
    person = {}
    person['name'] = input('Enter name: ')
    person['age'] = input('Enter age: ')
    person['phone'] = input('Enter phone: ')
    db[pid] = person

def lookup_person(db):
    pid = input('Enter ID nunber: ')
    field = input('What would you like to know? name, age or phone')
    field = field.strip().lower()
    print(db[pid][field])

def enter_command():
    cmd = input('Enter command for help: ')
    cmd = cmd.strip().lower()
    return cmd

if __name__ == '__main__':
    database = shelve.open('path')
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            else:
                assert 'Illegal command line'
    finally:
        database.close()


