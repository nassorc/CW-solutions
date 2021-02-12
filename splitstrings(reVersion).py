import re

def solution(s):
    Regex = re.compile(r'.{2}, s+"_"')
    ob = Regex.findall(s)
    return ob

s = 'abdhbdfh'
print(solution(s))