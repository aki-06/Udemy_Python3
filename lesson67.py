# import文とas
# import lesson_package.utils
# asはあまり多用しすぎない方が良い
# from lesson_package import utils as u
# 階層が増えたら.でつなぐ
from lesson_package.talk import human

# r = utils.say_twice('Hello')
# print(r)

print(human.sing())
print(human.cry())