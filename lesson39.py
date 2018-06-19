# while, else文
count = 0

# while count < 5:
#     print(count)
#     count += 1
# else:
#     print('done')

"""
breakは全てのループから抜ける
"""

while count < 5:
    if count == 1:
        break
    print(count)
    count += 1
else:
    print('done')
