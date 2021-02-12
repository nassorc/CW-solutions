def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    l = []
    for word in title:
        if word in minor_words:
            l.append(word)
        else:
            l.append(word.capitalize())
    return ' '.join(l)

print(title_case('The word and a beaver', 'a and'))
