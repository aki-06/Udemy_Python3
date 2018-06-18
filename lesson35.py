y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

# この書き方はあまり好ましくない
if not a == b:
    print('not equal')

# こちらの方が良い
if a != b:
    print('not equal')

# bool型でnotを使う
is_ok = True

if is_ok:
    print('ok')

is_ok = False

if not is_ok:
    print('NG')