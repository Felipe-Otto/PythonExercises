phrase = input('Type a phrase: ').strip().upper()
print('The letter "A" appears {} times.\nThe letter "A" appears in first at {}° position.\nThe letter "A" appears in last at {}° position'.format(phrase.count('A'), phrase.find('A') + 1, phrase.rfind('A') + 1))