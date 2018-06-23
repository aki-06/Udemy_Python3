# クロージャー

def outer(a, b):

    def inner():
        return a + b

    return inner

# <function outer.<locals>.inner at 0x103dc71e0>
# print(outer(1, 2))

f = outer(1, 2)
r = f()

# 3
print(r)

print('*' * 30)

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area

cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.141592)

print(cal1(10))
print(cal2(10))