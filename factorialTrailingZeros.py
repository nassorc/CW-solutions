def zeros(n):
    # total = 1
    # for i in range(n, 0, -1):
    #     total *= i
    # return total
    pow_of_5 = 5
    zeros = 0
    
    while n >= pow_of_5:
        zeros += n // pow_of_5
        pow_of_5 *= 5
        
    return zeros
   

# print(zeros(1))

for i in range(16):
    print('Fact: {} == {}'.format(i, zeros(i)))