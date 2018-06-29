# 特殊メソッド

class Word(object):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'test!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

w = Word('test')
w2 = Word('#######')
# print(len(w))
print(w + w2)