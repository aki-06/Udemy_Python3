# ジェネレーター

# for文
l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)


print('*' * 30)

# ジェネレーター
def counter(num=10):
    for _ in range(num):
        yield 'run'

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'


g = greeting()
c = counter()
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(g))
print('hello')
print(next(g))