# リストの操作

s = ['a', 'b', 'c', 'd', 'e']
s[0] = 'X'
print(s)

s[1:4] = ['B', 'C', 'D']
print(s)

i = [1, 2, 3, 4, 5]
i.append(100)
print(i)

i.pop()
print(i)

i.insert(0, 100)
print(i)

del i[0]
print(i)

# リストの結合
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

c = a + b
print(c)

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
x.extend(y)
print(x)