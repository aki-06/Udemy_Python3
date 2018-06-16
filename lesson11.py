# 文字列

print('test')
print("test")

print("I don't know")
print('I don\'t know')
print('say "I don\'t know"')
print("say \"i don'n know\"")

print('Hello. How are you?')
# \n:改行
print('Hello.\nHow are you?')

# windowsのpathの例
print('C:\name\name')
print(r'C:\name\name')

# 複数行書く際に自動的に改行
print("""
line1
line2
line3
""")

# 空白行無しにする
print('################')
print("""\
line1
line2
line3\
""")
print('################')


# 文字列の連結
print('Hi.' * 3 + 'Mike')
print('Py' + 'thon')
print('Py''thon')
s = ('AAAAAAAAA'
     'BBBBBBBBB')
print(s)


s = 'aaaaaaaaaa'\
    'bbbbbbbbbb'
print(s)