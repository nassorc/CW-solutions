def pig(text):
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in text.split()])

    

text = 'O tempora o mores !' # igpay atinlay siay oolcay
print(pig(text))
