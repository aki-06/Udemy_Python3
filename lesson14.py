# 文字列の代入

s = 'a is {}'.format('test')
print(s)

s = '{}{}{}'.format(1, 2, 3)
print(s, type(s))

greet = 'My name is {name} {family}'.format(name='Akihiro', family='Nemoto')
print(greet)