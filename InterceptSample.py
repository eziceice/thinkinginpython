class People:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __getattribute__(self, obj):
        if obj == 'age':
            print("被询问了年龄:")
            return super().__getattribute__(obj)
        elif obj == 'name':
            print('被询问了名字')
            return super().__getattribute__(obj)
        else:
            return super().__getattribute__(obj)

p = People(17, 'Test')
print(p.age)
print(p.name)
