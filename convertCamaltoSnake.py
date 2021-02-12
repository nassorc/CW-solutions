def convert(s):
    converted = s[0].lower()
    for char in s[1:]:
        if char.isupper():
            converted += '_{}'.format(char.lower())
        else:
            converted += char
     return converted

s = 'HelloWord'
print(convert(s))

# s = 'HelloWorld'
# camel = s[0].lower()
# for char in s[1:]:
#     if char.isupper():
#         camel += '_{}'.format(char.lower())
#     else:
#         camel += char

# print(camel)
    
