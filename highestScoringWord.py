def high(x):
    big = 0
    value = 0
    for word in x.split():
        for char in word:
            value += ord(char) - 96
        if value > big:
            w = word
            big = value
        value = 0
    return w
            

tx = 'aa'
txt = 'man i need a taxi up to ubud'
print(high(txt))
