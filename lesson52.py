# キーワード引数の辞書化

# **kwargsでキーワード引数の辞書化を行う
def menu(**kwargs):
    # {'entree': 'beef', 'drink': 'coffee'}
    # print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

# menu(entree='beef', drink='coffee')

d = {
    'entree': 'beef',
    'drink': 'soda',
    'dessert': 'ice'
}

menu(**d)

# *argsと**kwargsの順序に注意
def menu1(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu1('banana', 'apple', 'orange', entree='beef', drink='coke')