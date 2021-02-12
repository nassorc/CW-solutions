def fnr(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string.lower().count(letter) == 1:
            return string[i]

    return ''

s = 'stress'
print(fnr(s)) 

