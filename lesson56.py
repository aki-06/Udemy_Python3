# デコレータ

def print_more(func):
    def wrapper(*args, **kwargs):
        print('name = ', func.__name__)
        print('args = ', args)
        print('kwargs = ', kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_more
@print_info
def add_num(a, b):
    return a + b

# 上記と同じ意味
f = print_info(print_more(add_num))
r = f(30, 40)
print(r)

print('*' * 30)

r = add_num(10, 20)
print(r)