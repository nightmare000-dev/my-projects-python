en_chars = 'qwertyuiopasdfghjklzxcvbnm'
ru_chars = 'йцукенгшщзфывапролдячсмить'
dictionary = dict(zip(en_chars, ru_chars))

en_txt = input('EN: ').lower()
ru_txt = ''

for i in en_txt:
    if i in dictionary: ru_txt += dictionary[i]
    elif i == ' ': ru_txt += i
    elif i in '!@*^%$+=': ru_txt += i
    else: ru_txt += '?'
    
print(f'RU: {ru_txt}')