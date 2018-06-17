# タプル型

t = (1, 2, 3)
print(t)

print(t[1])

t = ([1, 2, 3], [4, 5, 6])
print(t)
t[0][0] = 100
print(t)

new_tuple = (1, 2, 3) + (4, 5, 6)
print(new_tuple)