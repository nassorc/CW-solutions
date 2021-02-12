def checker(string):
    count = 0
    for char in string:
        if char == '(': count += 1
        if char ==')': count-=1
        if count < 0: return False
    return True if count == 0 else False

print(checker('((()))()'))