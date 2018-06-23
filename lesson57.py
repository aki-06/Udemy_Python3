# ラムダ

l = ['mon', 'The', 'wed', 'Thu', 'fri', 'Sat', 'sun']

def change_words(words, func):
    for word in words:
        print(func(word))


# def sample_func(word):
#     return word.capitalize()

# sample_func = lambda word: word.capitalize()

change_words(l, lambda word: word.capitalize())
print('*' * 30)
change_words(l, lambda word: word.lower())