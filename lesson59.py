# リスト内包表記
t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)
r = []

for i in t:
    if i % 2 == 0:
        r.append(i)

print(r)

# 上記をリスト内包表記で書く
r = [i for i in t if i % 2 == 0]
print(r)

print('*' * 30)

r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)

r = [i * j for i in t for j in t2]
print(r)

# for文が複数繰り返される場合はリスト内包表記を多用しない
# 見やすいコードを意識することが大事