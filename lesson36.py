# 値が入っていない判定をするテクニック

is_ok = ['aa', 'bb']

# 0, 0.0, (), [], {}, False, set()は全てFalseと判定される
if is_ok:
    print('OK')
else:
    print('NG')