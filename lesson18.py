# リストのコピー

i = [1, 2, 3, 4, 5]
j = i

print('j = ', j)
print('i = ', i)

j[0] = 100

print('j = ', j)
print('i = ', i)


x = [1, 2, 3, 4, 5]
y = x.copy()
# y = x[:]

y[0] = 100

print('y = ', y)
print('x = ', x)

# 値渡し
X = 20
Y = X
Y = 5
print(id(X))
print(id(Y))
print(X)
print(Y)

# 参照渡し
x = ['a', 'b']
y = x
y[0] = 'p'
print(id(x))
print(id(y))
print(x)
print(y)