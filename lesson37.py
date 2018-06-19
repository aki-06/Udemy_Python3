# Noneを判定する場合

is_empty = None
# print(help(is_empty))

if is_empty is None:
    print('None!!!')

"""
==は値を比較する
isはオブジェクトを比較する.Noneを判定する時によく使う
"""
print(1 == True)
print(None is None)
print(1 is True)