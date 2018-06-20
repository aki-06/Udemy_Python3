# zip関数

days = ['Mon', 'Thu', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

# for i in range(len(days)):
#     print(days[i], fruits[i], drinks[i])

# スッキリしたコードになる
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)