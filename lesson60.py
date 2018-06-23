# 辞書包括表記

w = ['mon', 'the', 'wed']
f = ['coffee', 'tea', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

print('*' * 30)

d = {x: y for x, y in zip(w, f)}
print(d)