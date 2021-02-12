def digital(n):
    values = str(n)
    total = 0

    while len(values) != 1:
        for num in values:
            total = total + int(num)
        values = str(total)
        total = 0
    return int(values)




n = 942
print(digital(n))

