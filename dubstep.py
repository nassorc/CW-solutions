def song_decoder(song):
    return " ".join(song.replace('WUB', ' ').split())



string = 'AWUBWUBWUBBWUBWUBWUBC'

string = string.replace('WUB', ' ')
print(string)

string = string.split()
print(string)

string = ' '.join(string)
print(string)

# print(song_decoder(string))
