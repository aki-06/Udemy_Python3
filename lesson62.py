# ジェネレーター内包表記

def g():
    for i in range(10):
        yield i

g = g()
print(next(g))
print(next(g))
print(next(g))

print('*' * 30)

# tupleにする場合
# g = tuple(i for i in range(11, 20) if i % 2 == 0)
g = (i for i in range(11, 20) if i % 2 == 0)
print(type(g))
print(next(g))
print(next(g))


