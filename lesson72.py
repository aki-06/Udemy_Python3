# 組み込み関数

"""
https://docs.python.jp/3/library/functions.html
"""

ranking = {
    'A': 100,
    'B': 80,
    'C': 90
}

# print(ranking)
#
# for k in ranking:
#     print(k)

# print(ranking.get('A'))

print(sorted(ranking, key=ranking.get, reverse=True))