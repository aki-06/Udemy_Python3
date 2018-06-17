# 辞書型
d = {'x': 10, 'y': 20}
print(d)

d['x'] = 'XXX'
print(d)

d['z'] = 1000
print(d)

# dictの作り方は複数ある
d2 = dict(a=10, b=20)
print(d2) # {'a': 10, 'b': 20}

d3 = dict([('a', 10), ('b', 20)])
print(d3) # {'a': 10, 'b': 20}