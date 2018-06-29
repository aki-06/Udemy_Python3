# ファイルの作成

f = open('test.text', 'w')
f.write('test\n')
print('i am print', file=f)
print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)
f.close()