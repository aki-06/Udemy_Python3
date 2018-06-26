# ImportErrorの使い所
# バージョンが変わる場合や、import先が変わる場合の書き方
try:
    from lesson_package import utils
except ImportError:
    from lesson_package.tools import utils

h = utils.say_twice('Hello')
print(h)