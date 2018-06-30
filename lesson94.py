# 書き込み読み込みモード

s = """\
AAA
BBB
CCC
DDD
"""

# 書き込みと読み込みを同時に行うには'w+'とする
with open('test.txt', 'w+') as f:
    f.write(s)
    # 先頭に戻る
    f.seek(0)
    print(f.read())

print('########')

# 読みこんでから書き込む
with open('test.txt', 'r+') as f:
    print(f.read())
    f.seek(0)
    f.write(s)