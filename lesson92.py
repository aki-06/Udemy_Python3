# ファイルの読み込み
s = """\
AAA
BBB
CCC
DDD
"""

# 書き込み
# with open('test.txt', 'w') as f:
#     f.write(s)

# 読み込み
with open('test.txt', 'r') as f:
    print(f.read())

print('###########')

# 一行ずつ読み込む
with open('test.txt', 'r') as f:
    while True:
        line = f.readline()
        print(line, end='')
        if not line:
            break


print('###########')
# chunkごとに読み込む
with open('test.txt', 'r') as f:
    while True:
        chunk = 2
        line = f.readline(chunk)
        print(line)
        if not line:
            break
