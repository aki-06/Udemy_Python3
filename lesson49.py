# 位置引数、キーワード引数、デフォルト引数

def menu(entree, drink, dessert):
    print('entree = ' + entree)
    print('drink = ' + drink)
    print('dessert = ' + dessert)

# 位置引数は順序を間違うと正しいアウトプットが出ないので注意
menu('beef', 'beer', 'ice')

print('*' * 30)

# キーワード引数を使うと順序が異なる場合でも正しく出力される
menu(drink='tea', dessert='chocolate', entree='beef')

print('*' * 30)


# デフォルト引数
def menu1(entree='chicken', drink='wine', dessert='ice'):
    print('entree = ' + entree)
    print('drink = ' + drink)
    print('dessert = ' + dessert)

# デフォルト引数が出力される
menu1()

print('*' * 30)

# 引数で指定した値が出力される
menu1(entree='beef')