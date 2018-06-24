# 例外処理
l = [1, 2, 3]
i = 5

try:
    print(l[0])
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
else:
    print('done')
finally:
    print('clean up')