# 辞書をfor文で処理する
d = {'x': 100, 'y':200}

# for v in d:
#     print(v)

# リストの中にタプルを作る
print(d.items())

for k, v in d.items():
    print(k, ':', v)