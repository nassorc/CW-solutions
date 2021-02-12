s = ''
def solution(s):
    l = []
    nl = []

    for i in s:
        l.append(i)
    if len(l)%2==1:
        l.append('_')
    for i in range(0, len(l), 2):
        nl.append(l[i] + l[i+1])

    return nl

print(solution(s))
