# 位置引数のタプル化

# *argsで複数の引数をタプル化する
def say_something(*args):
    for arg in args:
        print(arg)


say_something('Hi', 'Mike', 'Nancy')