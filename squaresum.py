def move_zeros(arr):
    index = 0
    x = []
    for i in arr:
        if i == 0:
            x.append(arr.pop(index))
        index = index + 1

    return arr + x


print(move_zeros(['a', 1,0,2,0,4,0,2,4,5,6,0]))

