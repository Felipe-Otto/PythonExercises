variable = input('Type anything: ')
print('The type of the typed variable is {}.'.format(type(variable)))
print('The variable typed is a number: {}.'.format(variable.isnumeric()))
print('The variable typed is alphabetic: {}.'.format(variable.isalpha()))
print('The variable typed is alphanumeric: {}.'.format(variable.isalnum()))
print('The variable typed is composed only of space: {}.'.format(variable.isspace()))
print('The variable typed is in capital letters: {}.'.format(variable.isupper()))
print('The variable typed is in small letters: {}.'.format(variable.islower()))
print('The variable typed is capitalized: {}.'.format(variable.istitle()))
