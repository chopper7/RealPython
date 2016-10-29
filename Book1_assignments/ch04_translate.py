leetspeak = {'a': '4', 'b': '8', 'e': '3', 'l': '1',
             'o': '0', 's': '5', 't': '7'}

inp = input('Enter some text: ')

translation = inp[:]

for key in leetspeak:
    if key in inp:
        translation = translation.replace(key, leetspeak[key])


'''
translation = inp.replace('a', '4')
translation = translation.replace('b', '8')
translation = translation.replace('e', '3')
translation = translation.replace('l', '1')
translation = translation.replace('o', '0')
translation = translation.replace('s', '5')
translation = translation.replace('t', '7')
'''

print(translation)
