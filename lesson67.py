# import文とas
# import lesson_package.utils
# asはあまり多用しすぎない方が良い
# from lesson_package import utils as u
# 階層が増えたら.でつなぐ
from lesson_package.talk import human
from lesson_package.talk import animal
# *を用いたimportも避ける
# __init__.pyに記述したファイルを読み込める
# from lesson_package.talk import *
# r = utils.say_twice('Hello')
# print(r)

print(animal.sing())
print(animal.cry())

# print(human.sing())
# print(human.cry())