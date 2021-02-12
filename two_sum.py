def two_sum(number, target):
    l = []
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            check = number[i]+number[j]
            if check == target:
                l.append(i)
                l.append(j)
    if len(l) < 1:
        return None
    else:
        return l


# print(two_sum([0,0,3], 3))

for x,y in enumerate([0,1,2], 3):
    print(x)
    print(y)


# print(str(number[i]) + ' ' + str(number[i]+1) + ' = ' + str(number[i]+number[i]+1  ))
#         if number[i] + number[i]+1 == target:
#             print(number[i])
#             print(number[i]+1)