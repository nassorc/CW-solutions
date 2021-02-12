def generate_hashtag(s):
    x = []
    if s == "":
        return False
    else:
        for char in s.split():
            x.append(char.capitalize())
        return '#' + ''.join(x)


string = 'codewar coder and vscode'
print(generate_hashtag(string))





