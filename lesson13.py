s = 'My name is Mike. Hi Mike.'
print(s)

# 'My'から開始されているか
is_start = s.startswith('My')
print(is_start)

is_start = s.startswith('X')
print(is_start)

print('###############')
# どこに指定の文字列があるか
print(s.find('Mike')) # 前から何文字目か
print(s.rfind('Mike')) # 後ろから何文字目か

# 'Mike'は何個あるか
print(s.count('Mike'))

# 先頭以外小文字になる
print(s.capitalize())

# 全ての先頭の文字が大文字になる
print(s.title())

# 全ての文字が大文字になる
print(s.upper())

# 全ての文字が小文字になる
print(s.lower())

# 文字列を置き換える
print(s.replace('Mike', 'Nancy'))