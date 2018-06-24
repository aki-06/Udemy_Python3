# 名前空間とスコープ

animal = 'cat'

def f():
    global animal
    animal = 'dog'
    print(animal)
    print('local: ', locals())

f()
print(animal)
print(f.__name__)
print('global: ', globals())
