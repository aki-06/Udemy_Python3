# 独自例外の作成
class UppercaseError(Exception):
    pass


def check():
    words = ['apple', 'BANANA', 'orange']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

check()