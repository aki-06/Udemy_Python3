# 辞書型のメソッド
d = {'x': 10, 'y': 20}
d2 = {'x': 1000, 'j': 500}
d.update(d2)
print(d) # {'x': 1000, 'y': 20, 'j': 500}

d.pop('x')
print(d) # {'y': 20, 'j': 500}

print(d['y'])
print(d.get('y'))
r = d.get('z')
print(r) # None

d.clear()
print(d)


d = {'x': 10, 'y': 20}
print('a' in d) # False
print('x' in d) # True

print('#######################')
# 辞書のコピー
x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)