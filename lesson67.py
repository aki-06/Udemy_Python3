# import文とas
# import lesson_package.utils
from lesson_package import utils
# asはあまり多用しすぎない方が良い
# from lesson_package import utils as u

r = utils.say_twice('Hello')
print(r)