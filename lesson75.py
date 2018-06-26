# importする際の記述の仕方
"""
- アルファベット順に上から記述する
- 標準ライブラリとサードパーティのimportは行を空ける
- サードパーティと自分たちで開発したパッケージを記述する際も行を空ける
"""

# 標準ライブラリ
import collections
import os
import sys

# サードパーティ
import termcolor

# 自分達のパッケージ
import lesson_package

# ローカルファイル
import config

# インストールされているpathを表示
print(collections.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)
print(config.__file__)

print(sys.path)