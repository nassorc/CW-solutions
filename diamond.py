def diamond(n):
    s = []
    count = 0 - 1
    if n%2==0 or n < 0:
        return None
    for i in range(1, n + 1):
        if i%2 == 1:
            count = count  + 1 

    for i in range(1,n+1,2):
        s.append(' '*(count) + '*'*(i) + '\\n')
        count -= 1
    count = 0
    for i in range(n,0,-2):
        if i == 1:
            break
        s.append(' '*(count+1) + '*'*(i-2) + '\\n')
        count += 1

    return ''.join(s)

print(diamond(3))

# Shorter version
'''
def diamond(n):
    if n > 0 and n % 2 == 1:
        diamond = ""
        for i in range(n):
            diamond += " " * abs((n/2) - i)
            diamond += "*" * (n - abs((n-1) - 2 * i))
            diamond += "\n"
        return diamond
    else:
        return None
'''
