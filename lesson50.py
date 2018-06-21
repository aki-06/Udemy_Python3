# デフォルト引数で気をつけること
"""
Pythonではリストや辞書をのデフォルト引数で与えるべきではない
"""
# バグに繋がる
def test_func(x, l=[]):
    l.append(x)
    return l

# y = [1, 2, 3]
# r = test_func(100, y)
# print(r)
#
# y = [1, 2, 3]
# r = test_func(200, y)
# print(r)

r = test_func(100)
print(r)

r = test_func(100)
print(r)

# デフォルト引数にNoneを与えておく
def test_func1(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

r = test_func1(100)
print(r)

r = test_func1(100)
print(r)

y = [1, 2, 3]
r = test_func1(100, y)
print(y)