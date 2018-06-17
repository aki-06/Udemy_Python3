# タプルのアンパッキング

num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x)
print(y)

min, max = 0, 100
print(min, max)

i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)

x = 100
y = 200

x, y = y, x
print(x, y)