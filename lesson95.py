# テンプレート
import string

# s = """\
#
# Hi $name.
#
# $contents
#
# Have a good day
# """

# t = string.Template(s)
# contents = t.substitute(name='Mike', contents='How are you?')
# print(contents)

with open('Design/design.txt') as f:
    t = string.Template(f.read())

contents = t.substitute(name='Mike', contents='Hello')
print(contents)