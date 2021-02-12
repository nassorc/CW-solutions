def solution(array_a, array_b):
    temp = 0
    compute = 0
    for i, j in list(zip(array_a, array_b)):
        compute = ((i-j)*1)
        if compute < 0:
            compute *= -1
        temp += (compute ** 2)

    return temp/len(array_a)

print(solution([1,2,3], [4,5,6]))