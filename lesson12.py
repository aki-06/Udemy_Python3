# 文字列のインデックスとスライス

word = 'Python'
print(word[0])
print(word[1])
print(word[-1])
print('################')
print(word[0:3])
print(word[:3])
print('################')
print(word[2:])
print('################')
word = 'J' + word[1:]
print(word)
print(word[:]) # 全てのコピー
print('################')
# インデックスの長さ
n = len(word)
print(n)