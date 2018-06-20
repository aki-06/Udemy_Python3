# for文、continue文、break文

some_list = [1, 2, 3, 4, 5]

# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1

# for i in some_list:
#     print(i)


for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        continue
    elif word == 'Mike':
        break
    print(word)