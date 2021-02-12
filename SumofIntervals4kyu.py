def sum(intervals):
    total = 0
    max = intervals[0][1]
    min = intervals[0][0]
    print(min)
    for pair in intervals:
        if max in range(pair[0], pair[1]): # max >= pair[0] and max <= pair[1]
            if min >= pair[0]:
                min = pair[0]


    for pair in intervals:
        print('first:', pair[1], 'second:', pair[0], '=', pair[1]-pair[0])
        total += pair[1] - pair[0]
        print(total)
    return total

print(sum([(1, 4), (7, 10), (3, 5)])) 
print(sum([(1, 5), (1, 5)]))