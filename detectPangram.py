import string 
import re

def is_pangram(s):
    sRegex =  re.compile(r'\d.*[(a-zA-Z)]')
    so = sRegex.findall(s)
    print(so)
    if so:
        return True

print(is_pangram("The quick brown fox jumps over the lazy dog"))
