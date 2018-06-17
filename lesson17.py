# リストのメソッド

r = [1, 2, 3, 4, 5, 1, 2, 3]
# 値がどこにあるか探す
print(r.index(3)) # 2
print(r.index(3, 3)) # 7

# リスト内にある値の数
print(r.count(3)) # 2

# ソート
r.sort()
print(r) # [1, 1, 2, 2, 3, 3, 4, 5]

# 逆にソート
r.sort(reverse=True)
print(r) # [5, 4, 3, 3, 2, 2, 1, 1]

# 元に戻す
r.reverse()
print(r) # [1, 1, 2, 2, 3, 3, 4, 5]

# split
s = 'My name is Mike.'
to_split = s.split(' ') # 空白で区切る
print(to_split) # ['My', 'name', 'is', 'Mike.']

# 元に戻す
x = ' '.join(to_split)
print(x)

# ドキュメント
print(help(list))
